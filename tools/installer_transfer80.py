"""Reassemble existing installer bytes only; no build or product execution."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib,json,subprocess,tempfile,time
REPO='Elviszhuoyu/VidSage-Releases'
TAG='v0.1.80'
RELEASE='416487307'
NAME='VidSage-0.1.80-win11-x64-Setup.exe'
SHA='aa9d787103af26e4771dc499dbea0e17b485e61a8911440e64a5fc5e55b2a549'
SIZE=951393454
MANIFEST='setup80-transfer-manifest.json'
MANIFEST_SHA='e40a66d1cb9c9f06e653763f96a55e3f638f3cb278c17270a98f8afcf54b26aa'
ROOT=Path(tempfile.mkdtemp(prefix='vidsage-installer-transfer80-'))
def gh(*args):
 return subprocess.check_output(['gh',*args],text=True)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def assets():
 r=json.loads(gh('api','repos/'+REPO+'/releases/'+RELEASE))
 assert r['draft'], 'The release must remain draft until transfer cleanup is complete'
 return {a['name']:a for a in r['assets']}
def matches(a,row):
 return a['state']=='uploaded' and a['size']==row['bytes'] and a['digest']=='sha256:'+row['sha256']
for attempt in range(160):
 remote=assets()
 if MANIFEST in remote:
  assert remote[MANIFEST]['digest']=='sha256:'+MANIFEST_SHA
  gh('release','download',TAG,'--repo',REPO,'--pattern',MANIFEST,'--dir',str(ROOT))
  break
 time.sleep(45)
else:raise RuntimeError('Transfer manifest timed out')
assert sha(ROOT/MANIFEST)==MANIFEST_SHA
m=json.loads((ROOT/MANIFEST).read_text(encoding='utf-8'))
assert (m['filename'],m['bytes'],m['sha256'])==(NAME,SIZE,SHA)
assert len(m['parts'])==57 and sum(p['bytes'] for p in m['parts'])==SIZE
assert [p['filename'] for p in m['parts']]==['setup80-transfer-%03d.part'%i for i in range(57)]
last=-1
for attempt in range(160):
 remote=assets()
 complete=sum(p['filename'] in remote and matches(remote[p['filename']],p) for p in m['parts'])
 if complete!=last:print('Verified transfer parts: %s / 57'%complete,flush=True);last=complete
 if complete==57:break
 time.sleep(45)
else:raise RuntimeError('Transfer parts timed out; completed parts remain resumable')
def get(row):
 gh('release','download',TAG,'--repo',REPO,'--pattern',row['filename'],'--dir',str(ROOT))
 p=ROOT/row['filename']
 assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
 return p
with ThreadPoolExecutor(max_workers=4) as pool:parts=list(pool.map(get,m['parts']))
output=ROOT/NAME
with output.open('wb') as f:
 for p in parts:
  with p.open('rb') as src:
   while b:=src.read(4*1024**2):f.write(b)
assert output.stat().st_size==SIZE and sha(output)==SHA
remote=assets()
if NAME in remote:assert matches(remote[NAME],{'bytes':SIZE,'sha256':SHA})
else:gh('release','upload',TAG,'--repo',REPO,str(output))
remote=assets();assert matches(remote[NAME],{'bytes':SIZE,'sha256':SHA})
# Remove only this run's exact verified temporary assets after the final installer is accepted.
for row in m['parts']+[{'filename':MANIFEST,'bytes':(ROOT/MANIFEST).stat().st_size,'sha256':MANIFEST_SHA}]:
 a=remote[row['filename']];assert matches(a,row)
 gh('api','--method','DELETE','repos/'+REPO+'/releases/assets/'+str(a['id']))
print(json.dumps({'status':'installer-transferred-and-temporary-assets-removed','filename':NAME,'bytes':SIZE,'sha256':SHA,'parts':57,'productRebuilt':False}),flush=True)
