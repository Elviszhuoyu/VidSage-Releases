"""Transfer already-built 0.2.1 bytes; validate before upload or temporary-asset cleanup."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib,json,re,subprocess,sys,tempfile,time
REPO='Elviszhuoyu/VidSage-Releases'
RELEASE=421962988
TAG='v0.2.1'
MANIFEST='transfer021-manifest.json'
MANIFEST_SHA='8af2b5b895f5659593d85589df754aaf2f76794a6563df8226671f895f40c28b'
EXPECTED={'VidSage-0.2.1-win11-x64-Setup.exe': (951948155, '9cec357ca385a536b3f7b38976df8e9e12916851dad36bd62ca5a4333c3d5d44')}
def gh(*args):return subprocess.check_output(['gh',*map(str,args)],text=True)
def digest(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def matches(a,row):return a['state']=='uploaded' and a['size']==row['bytes'] and a['digest']=='sha256:'+row['sha256']
def assets():
 r=json.loads(gh('api',f'repos/{REPO}/releases/{RELEASE}'))
 assert r['draft'] and r['tag_name']==TAG,'Release must remain the approved draft'
 return {a['name']:a for a in r['assets']}
def assemble(row,parts,output):
 with output.open('wb') as out:
  for part in row['parts']:
   source=parts/part['filename'];assert source.stat().st_size==part['bytes'] and digest(source)==part['sha256']
   with source.open('rb') as src:
    while block:=src.read(4*1024**2):out.write(block)
 assert output.stat().st_size==row['bytes'] and digest(output)==row['sha256']
def self_test():
 root=Path(tempfile.mkdtemp(prefix='transfer021-test-'));data=b'firstsecond';rows=[]
 for i,b in enumerate([b'first',b'second']):
  p=root/f'part{i}';p.write_bytes(b);rows.append({'filename':p.name,'bytes':len(b),'sha256':digest(p)})
 row={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'parts':rows};assemble(row,root,root/'out');assert (root/'out').read_bytes()==data
 (root/'part0').write_bytes(b'bad')
 try:assemble(row,root,root/'bad-out')
 except AssertionError:pass
 else:raise AssertionError('Corrupt part accepted')
 print('Byte-identical assembly and corruption rejection passed',flush=True)
def main():
 root=Path(tempfile.mkdtemp(prefix='vidsage-transfer021-'));last=None
 for _ in range(180):
  remote=assets()
  if MANIFEST in remote:
   assert remote[MANIFEST]['digest']=='sha256:'+MANIFEST_SHA
   gh('release','download',TAG,'--repo',REPO,'--pattern',MANIFEST,'--dir',root);break
  time.sleep(30)
 else:raise RuntimeError('No verified manifest; draft preserved')
 assert digest(root/MANIFEST)==MANIFEST_SHA
 manifest=json.loads((root/MANIFEST).read_text(encoding='utf-8'));assert manifest['schema']==1 and manifest['releaseId']==RELEASE and manifest['releaseTag']==TAG
 assert {f['filename'] for f in manifest['files']}==set(EXPECTED)
 for index,row in enumerate(manifest['files']):
  assert (row['bytes'],row['sha256'])==EXPECTED[row['filename']]
  kind='setup' if row['filename'].endswith('.exe') else 'content'
  assert len(row['parts']) == 57 and sum(p['bytes'] for p in row['parts'])==row['bytes']
  for i,part in enumerate(row['parts']):assert part['filename']==f'transfer021-{kind}-{i:03d}.part' and 0<part['bytes']<=16*1024**2 and re.fullmatch('[0-9a-f]{64}',part['sha256'])
 rows=[p for f in manifest['files'] for p in f['parts']]
 for _ in range(180):
  remote=assets();complete=sum(p['filename'] in remote and matches(remote[p['filename']],p) for p in rows)
  if complete!=last:print(f'Verified transfer parts: {complete}/{len(rows)}',flush=True);last=complete
  if complete==len(rows):break
  time.sleep(30)
 else:raise RuntimeError('Incomplete transfer; verified parts and draft preserved')
 def get(row):
  gh('release','download',TAG,'--repo',REPO,'--pattern',row['filename'],'--dir',root)
  p=root/row['filename'];assert p.stat().st_size==row['bytes'] and digest(p)==row['sha256']
 with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(get,rows))
 for row in manifest['files']:
  output=root/row['filename'];assemble(row,root,output);remote=assets()
  if row['filename'] not in remote:gh('release','upload',TAG,'--repo',REPO,output)
  assert matches(assets()[row['filename']],row)
 # Delete only this manifest's exact verified temporary assets after both final files match.
 remote=assets();temporary=rows+[{'filename':MANIFEST,'bytes':(root/MANIFEST).stat().st_size,'sha256':MANIFEST_SHA}]
 for row in temporary:
  a=remote[row['filename']];assert matches(a,row);gh('api','--method','DELETE',f'repos/{REPO}/releases/assets/{a["id"]}')
 print(json.dumps({'passed':True,'files':list(EXPECTED),'parts':len(rows),'productRebuilt':False,'temporaryAssetsRemoved':True}),flush=True)
if __name__=='__main__':
 if '--self-test' in sys.argv:self_test()
 else:self_test();main()
