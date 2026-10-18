"""Assemble only pinned third-party sources; never execute their build scripts."""
from pathlib import Path, PurePosixPath
from concurrent.futures import ThreadPoolExecutor
import hashlib, io, json, os, re, shutil, subprocess, tarfile, tempfile, time, urllib.request, zipfile

REPO = 'Elviszhuoyu/VidSage-Releases'
TAG = 'v0.1.80'
INPUT = 'source-build-inputs-0.1.80.zip'
INPUT_SHA = 'bad5a8b2df95b4f537381d72135e38733c63fbbe83271066fef6b6e24440b7e1'
ROOT = Path(tempfile.mkdtemp(prefix='vidsage-source80-'))
DATA = ROOT / 'data'
OUT = ROOT / 'out'
DATA.mkdir(); OUT.mkdir()

def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def check(path, row):
    assert path.stat().st_size == row['bytes'], path.name
    assert sha(path) == row['sha256'], path.name

def safe(root, name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts and '\\' not in name, name
    target = root / p
    target.parent.mkdir(parents=True, exist_ok=True)
    return target

def run(*args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)

def download(row):
    target = safe(DATA / 'mpv', row['path'])
    assert row['url'].startswith('https://repo.msys2.org/mingw/sources/')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(row['url'], timeout=90) as r, target.open('wb') as f:
                shutil.copyfileobj(r, f, 4 * 1024**2)
            check(target, row)
            return
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))

def extract_zst(archive, destination):
    members = []
    with subprocess.Popen(['zstd', '-dc', str(archive)], stdout=subprocess.PIPE) as proc:
        with tarfile.open(fileobj=proc.stdout, mode='r|') as tf:
            for m in tf:
                target = safe(destination, m.name)
                assert m.isdir() or m.isfile(), m.name
                if m.isfile():
                    with tf.extractfile(m) as source, target.open('wb') as f:
                        shutil.copyfileobj(source, f, 4 * 1024**2)
                    target.chmod(m.mode & 0o777)
                    members.append((m.name, target))
        assert proc.wait() == 0
    return members

def record(path):
    return {'filename': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}

# A local uploader may still be completing this one small input asset.
for attempt in range(40):
    release = json.loads(subprocess.check_output(['gh', 'api', 'repos/' + REPO + '/releases/416487307']))
    if any(a['name'] == INPUT and a['state'] == 'uploaded' for a in release['assets']):
        break
    print('Waiting for the verified build-input asset', flush=True)
    time.sleep(30)
else:
    raise RuntimeError('Build input did not finish uploading within 20 minutes')
run('gh', 'release', 'download', TAG, '--repo', REPO, '--pattern', INPUT, '--dir', str(ROOT))
assert sha(ROOT / INPUT) == INPUT_SHA
with zipfile.ZipFile(ROOT / INPUT) as z:
    manifest = json.loads(z.read('manifest.json'))
    assert manifest['repository'] == REPO and manifest['releaseTag'] == TAG
    for a in manifest['assets']:
        for e in a['entries']:
            if e['route'] == 'bundled':
                p = safe(DATA / a['component'], e['path'])
                p.write_bytes(z.read(a['component'] + '/' + e['path']))
                check(p, e)
print('Pinned small inputs verified', flush=True)

mpv = next(a for a in manifest['assets'] if a['component'] == 'mpv')
with ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(download, [e for e in mpv['entries'] if e['route'] == 'official-msys2']))
print('All 104 original MSYS2 source packages verified', flush=True)
cache = ROOT / 'btbn-cache.zip'
with cache.open('wb') as f:
    run('gh', 'api', 'repos/BtbN/FFmpeg-Builds/actions/artifacts/12100414440/zip', stdout=f)
check(cache, manifest['sourceCache'])
inner = ROOT / 'cache.tar.gz'
with zipfile.ZipFile(cache) as z, z.open('cache.tar.gz') as src, inner.open('wb') as dst:
    shutil.copyfileobj(src, dst, 4 * 1024**2)
check(inner, manifest['sourceCacheInner'])
wanted = {e['cacheMember']: e for a in manifest['assets'] for e in a['entries'] if e['route'] == 'official-btbn-cache'}
with tarfile.open(inner, 'r|gz') as tf:
    for m in tf:
        if m.name in wanted:
            e = wanted.pop(m.name)
            assert m.isfile()
            p = safe(DATA / 'ffmpeg', e['path'])
            with tf.extractfile(m) as src, p.open('wb') as dst:
                shutil.copyfileobj(src, dst, 4 * 1024**2)
            check(p, e)
assert not wanted, list(wanted)
print('All 86 selected BtbN snapshots verified', flush=True)

# Reproduce the reviewed FFmpeg ZIPs exactly, including their original ZIP metadata.
outputs = []
for a in manifest['assets']:
    if a['component'] != 'ffmpeg':
        continue
    p = OUT / a['name']
    with zipfile.ZipFile(p, 'x', compression=zipfile.ZIP_STORED, allowZip64=True) as z:
        for e in a['entries']:
            info = zipfile.ZipInfo(e['path'], tuple(e['zipInfo']['date_time']))
            for key, value in e['zipInfo'].items():
                if key != 'date_time':
                    setattr(info, key, bytes.fromhex(value) if key in ('comment', 'extra') else value)
            info.file_size = e['bytes']
            with (DATA / 'ffmpeg' / e['path']).open('rb') as src, z.open(info, 'w') as dst:
                shutil.copyfileobj(src, dst, 4 * 1024**2)
    check(p, a)
    outputs.append(p)
    print('Exact original FFmpeg ZIP reproduced: ' + p.name, flush=True)

# Replace only the bare whisper.cpp history with every blob from the fixed tree.
slim = ROOT / 'slim'
slim.mkdir()
whisper_row = next(e for e in mpv['entries'] if '/mingw-w64-whisper.cpp-' in e['path'])
raw = ROOT / 'whisper-original'
extract_zst(DATA / 'mpv' / whisper_row['path'], raw)
original = raw / 'mingw-w64-whisper.cpp'
repo = original / 'whisper.cpp'
(repo / 'config').write_text('[core]\nrepositoryformatversion = 0\nbare = true\n', encoding='utf-8')
commit = 'da54572229bcf64ba367d96c7ef15770376c4280'
git = ['git', '-c', 'maintenance.auto=false', '-c', 'gc.auto=0', '-c', 'core.hooksPath=/dev/null', '--git-dir=' + str(repo)]
tree = subprocess.check_output(git + ['ls-tree', '-r', '-z', commit])
entries = []
for line in tree.split(b'\0'):
    if line:
        meta, name = line.split(b'\t', 1)
        mode, kind, oid = meta.decode('ascii').split()
        assert kind == 'blob' and mode in ('100644', '100755', '120000'), 'Unexpected gitlink or file type'
        entries.append((mode, oid, name.decode('utf-8')))
description = subprocess.check_output(git + ['describe', '--long', '--tags', commit], text=True).strip()
assert description == 'v1.9.4-77-gda5457222', description
fixed = slim / 'whisper.cpp'
fixed.mkdir()
source_tar = fixed / 'whisper.cpp-fixed.tar.gz'
with subprocess.Popen(git + ['cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
    with tarfile.open(source_tar, 'w:gz', compresslevel=6) as tf:
        for mode, oid, name in entries:
            safe(ROOT / 'path-validation-only', name)
            proc.stdin.write((oid + '\n').encode()); proc.stdin.flush()
            actual_oid, kind, size = proc.stdout.readline().decode('ascii').split()
            assert actual_oid == oid and kind == 'blob'
            data = proc.stdout.read(int(size)); assert proc.stdout.read(1) == b'\n'
            assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == oid
            ti = tarfile.TarInfo('whisper.cpp/' + name)
            ti.mtime = 0
            if mode == '120000':
                ti.type = tarfile.SYMTYPE; ti.linkname = data.decode('utf-8'); ti.mode = 0o777
                tf.addfile(ti)
            else:
                ti.mode = 0o755 if mode == '100755' else 0o644; ti.size = len(data)
                tf.addfile(ti, io.BytesIO(data))
    proc.stdin.close(); assert proc.wait() == 0
# Check every archived file against its original Git blob, including executable bits and symlinks.
expected = {name: (mode, oid) for mode, oid, name in entries}
with tarfile.open(source_tar, 'r:gz') as tf:
    for m in tf:
        name = m.name.removeprefix('whisper.cpp/')
        mode, oid = expected.pop(name)
        data = m.linkname.encode('utf-8') if m.issym() else tf.extractfile(m).read()
        assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == oid
        assert (m.issym() and mode == '120000') or (m.isfile() and oct(m.mode)[-3:] == mode[-3:])
assert not expected
recipe = (original / 'PKGBUILD').read_text(encoding='utf-8')
assert commit in recipe
modified, n = re.subn(r'^source=\(.*?\)$', 'source=("whisper.cpp-fixed.tar.gz")', recipe, count=1, flags=re.M | re.S)
assert n == 1
modified, n = re.subn(r'^sha256sums=\(.*?\)$', "sha256sums=('" + sha(source_tar) + "')", modified, count=1, flags=re.M | re.S)
assert n == 1
modified, n = re.subn(r'^pkgver\(\) \{.*?^\}', 'pkgver() {\n  echo "1.9.4.r77.gda5457222"\n}', modified, count=1, flags=re.M | re.S)
assert n == 1
assert modified[modified.index('build()'):]==recipe[recipe.index('build()'):]
(fixed / 'PKGBUILD').write_text(modified, encoding='utf-8')
shutil.copyfile(original / 'PKGBUILD', fixed / 'PKGBUILD.upstream')
shutil.copyfile(original / '.SRCINFO', fixed / 'SRCINFO.upstream')
whisper_proof = {'originalArchive': whisper_row['path'], 'originalSha256': whisper_row['sha256'], 'commit': commit, 'tree': subprocess.check_output(git + ['rev-parse', commit + '^{tree}'], text=True).strip(), 'gitDescribe': description, 'verifiedBlobCount': len(entries), 'gitlinks': 0, 'source': record(source_tar), 'recipeChanges': 'Local archive source/hash and fixed pkgver only; build/package bodies byte-identical; original PKGBUILD and SRCINFO retained.'}
print('whisper.cpp fixed tree and build recipe verified', flush=True)

# Store the identical LLVM upstream tarball once; retain both distinct recipes and patches.
llvm_rows = [e for e in mpv['entries'] if re.search(r'/mingw-w64-(llvm-openmp|libc\+\+)-22\.1\.8-1\.src', e['path'])]
assert len(llvm_rows) == 2
shared = slim / 'llvm/shared'; shared.mkdir(parents=True)
llvm_proof = []
for e in llvm_rows:
    temp = ROOT / ('llvm-' + str(len(llvm_proof)))
    members = extract_zst(DATA / 'mpv' / e['path'], temp)
    package = next(temp.iterdir())
    source = package / 'llvm-project-22.1.8.src.tar.xz'
    assert source.stat().st_size == 167061596
    common = shared / source.name
    if common.exists():
        assert sha(common) == sha(source)
    else:
        shutil.copyfile(source, common)
    dest = slim / 'llvm' / package.name; dest.mkdir()
    kept = []
    for name, file in members:
        if file == source:
            continue
        target = safe(dest, file.relative_to(package).as_posix())
        shutil.copyfile(file, target)
        kept.append({'path': target.relative_to(slim).as_posix(), 'sha256': sha(target)})
    llvm_proof.append({'originalArchive':e['path'], 'originalSha256':e['sha256'], 'package':package.name, 'sharedSourceSha256':sha(common), 'retainedFiles':kept})
(slim / 'llvm/restore.py').write_text('''from pathlib import Path
import hashlib, shutil
root = Path(__file__).resolve().parent
source = root / 'shared/llvm-project-22.1.8.src.tar.xz'
expected = ''' + repr(sha(common)) + '''
with source.open('rb') as f:
    assert hashlib.file_digest(f, 'sha256').hexdigest() == expected
for package in ('mingw-w64-llvm-openmp', 'mingw-w64-libc++'):
    target = root / package / source.name
    if target.exists():
        with target.open('rb') as f:
            assert hashlib.file_digest(f, 'sha256').hexdigest() == expected
    else:
        shutil.copyfile(source, target)
print('Both original package directories now contain the exact shared upstream archive.')
''', encoding='utf-8')
# Test the restore helper on copies so the delivered tree retains only one upstream archive.
restore_test = ROOT / 'restore-test'
shutil.copytree(slim / 'llvm', restore_test)
run('python3', str(restore_test / 'restore.py'))
for e in llvm_proof:
    assert sha(restore_test / e['package'] / common.name) == e['sharedSourceSha256']
proof = {'status':'source-content-verified-no-product-rebuild', 'originalMpvArchive':{'filename':mpv['name'],'sha256':mpv['sha256'],'bytes':mpv['bytes']}, 'whisper':whisper_proof, 'llvm':llvm_proof, 'unchangedSourceArchives':101, 'productInstallerChanged':False, 'thirdPartyBuildScriptsExecuted':False}
(slim / 'source-slim-verification.json').write_text(json.dumps(proof, indent=2)+'\n',encoding='utf-8')
(slim / 'README.md').write_text('''# Fixed MSYS2 corresponding sources

The 101 unchanged source packages remain in sources/. Three original source packages are represented by the complete material under slim/ instead. Existing source-acquisition and source-delivery manifests describe the original packages for provenance; slim/source-slim-verification.json describes these two storage transformations.

- whisper.cpp: every source blob, executable bit and symlink from commit da54572229bcf64ba367d96c7ef15770376c4280 is preserved in whisper.cpp/whisper.cpp-fixed.tar.gz. The local PKGBUILD replaces only the download source/checksum and git-derived pkgver; build and package bodies are unchanged. Use that directory with the usual MSYS2 makepkg environment. PKGBUILD.upstream and SRCINFO.upstream retain the original recipe and metadata. Only repository history was omitted.
- LLVM: run `python llvm/restore.py` to copy the single verified upstream archive into both original package directories. All distinct recipe, patch, signature and metadata files remain unchanged. Then use each directory with the usual MSYS2 makepkg environment.

The exact upstream URLs and hashes remain in source-acquisition.json. No application source, models for application users, user data or private history are included. These checks verify source preservation and packaging; they do not claim a new dependency build or bit-for-bit binary reproduction.
''',encoding='utf-8')
excluded={whisper_row['path']}|{e['path'] for e in llvm_rows}
p = OUT / 'msys2-mpv-0.41.0-8-sources-slim.zip'
with zipfile.ZipFile(p,'x',compression=zipfile.ZIP_STORED,allowZip64=True) as z:
    for e in mpv['entries']:
        if e['path'] not in excluded:
            source = DATA/'mpv'/e['path']; check(source,e); z.write(source,e['path'])
    for source in sorted(slim.rglob('*')):
        if source.is_file():
            z.write(source,'slim/'+source.relative_to(slim).as_posix())
with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
outputs.append(p)
report = {'schemaVersion':1,'inputSha256':INPUT_SHA,'assets':[record(p) for p in outputs],'slimming':proof,'originalMpvBytes':mpv['bytes'],'slimMpvBytes':p.stat().st_size,'savedMpvBytes':mpv['bytes']-p.stat().st_size,'ffmpegOriginalZipHashesMatched':True}
report_path = OUT / 'source-cloud-verification.json'
report_path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
for p in outputs+[report_path]:
    run('gh','release','upload',TAG,'--repo',REPO,str(p))
print(json.dumps(report,indent=2),flush=True)
