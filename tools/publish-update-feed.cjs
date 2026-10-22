const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),cp=require('node:child_process');
function contentPackVersion(pack,target){
 const version=pack?.version??target,parts=typeof version==='string'?version.split('.').map(Number):[],latest=target.split('.').map(Number);
 if(typeof version!=='string'||!/^\d+\.\d+\.\d+$/.test(version)||parts.some(n=>!Number.isSafeInteger(n))||(parts[0]-latest[0]||parts[1]-latest[1]||parts[2]-latest[2])>0||!new RegExp('^VidSage-'+version.replace(/\./g,'\\.')+'-content-\\d{3}\\.vsp$').test(pack.file))throw Error('Invalid content pack');
 return version;
}
async function verifyContentReferences(packs,version,repository,fetchRelease,head){
 const releases=new Map();
 for(const pack of packs){
  const origin=contentPackVersion(pack,version);if(!pack.version)continue;
  const tag='v'+origin;if(!releases.has(tag))releases.set(tag,await fetchRelease(tag));
  const release=releases.get(tag),asset=release?.assets?.find(a=>a.name===pack.file),url=`https://github.com/${repository}/releases/download/${tag}/${pack.file}`;
  if(release?.draft||release?.tag_name!==tag||!asset||asset.state!=='uploaded'||!Number.isSafeInteger(pack.bytes)||pack.bytes<1||!/^[a-f0-9]{64}$/.test(pack.sha256)||asset.size!==pack.bytes||asset.digest!=='sha256:'+pack.sha256||asset.browser_download_url!==url)throw Error('Historical content asset differs: '+pack.file);
  const response=await head(url);if(!response.ok||Number(response.headers.get('content-length'))!==pack.bytes)throw Error('Historical content asset unavailable: '+pack.file);
 }
}
function entries(releases,repository){
 const base=`https://github.com/${repository}/releases`;
 return releases.filter(r=>!r.draft&&/^v\d+\.\d+\.\d+$/.test(r.tag_name)).map(r=>{
  const version=r.tag_name.slice(1),name=`VidSage-${version}-win11-x64-Setup.exe`,asset=r.assets.find(a=>a.name===name&&a.state==='uploaded');
  if(r.html_url!==`${base}/tag/${r.tag_name}`||!asset||asset.browser_download_url!==`${base}/download/${r.tag_name}/${name}`||!/^sha256:[a-f0-9]{64}$/.test(asset.digest)||!Number.isSafeInteger(asset.size)||asset.size<=0)return null;
  return {tag_name:r.tag_name,draft:false,prerelease:r.prerelease,html_url:r.html_url,assets:[{name,state:'uploaded',browser_download_url:asset.browser_download_url,digest:asset.digest,size:asset.size}]};
 }).filter(Boolean).sort((a,b)=>{const x=a.tag_name.slice(1).split('.').map(Number),y=b.tag_name.slice(1).split('.').map(Number);return y[0]-x[0]||y[1]-x[1]||y[2]-x[2];}).slice(0,30);
}
function bindContent(entry,release,content,repository,historical=[]){
 if(!content)return;
 const version=entry.tag_name.slice(1),specs=[content.manifest,content.installer,...(content.packs||[])];
 if(content.manifest?.file!==`VidSage-${version}-content.json`||content.installer?.file!==`VidSage-${version}-win11-x64-Content-Setup.exe`||!Array.isArray(content.packs)||content.packs.length<1||content.packs.length>32)throw Error('Invalid content binding');
 for(const p of content.packs)contentPackVersion(p,version);
 const matched=specs.map(s=>{const origin=s.version??version,source=origin===version?release:historical.find(r=>r.tag_name==='v'+origin&&!r.draft),a=source?.assets.find(a=>a.name===s.file);if(!/^[a-f0-9]{64}$/.test(s.sha256)||!Number.isSafeInteger(s.bytes)||s.bytes<1||!a||a.state!=='uploaded'||a.digest!=='sha256:'+s.sha256||a.size!==s.bytes||a.browser_download_url!==`https://github.com/${repository}/releases/download/v${origin}/${s.file}`)throw Error('Incomplete content release: '+s.file);return a;});
 entry.assets.push(...matched.slice(0,2));entry.contentReady=true;
}
async function generate(repository,output){
 if(!/^[\w.-]+\/[\w.-]+$/.test(repository))throw Error('Invalid repository');
 let releases;
 if(process.env.GH_TOKEN){const response=await fetch(`https://api.github.com/repos/${repository}/releases?per_page=30`,{headers:{Authorization:`Bearer ${process.env.GH_TOKEN}`,Accept:'application/vnd.github+json'},signal:AbortSignal.timeout(30000)});if(!response.ok)throw Error('Release API status '+response.status);releases=await response.json();}
 else releases=JSON.parse(cp.execFileSync('gh',['api',`repos/${repository}/releases?per_page=30`],{encoding:'utf8',windowsHide:true}));
 const selected=entries(releases,repository);if(!selected.length)throw Error('No complete public Windows release');
 // Only the newest release needs a consent binding; historical links remain usable without it.
 for(const entry of selected.slice(0,1)){
  const release=releases.find(r=>r.tag_name===entry.tag_name),reference=release.assets.find(a=>a.name==='source-references.json'&&a.state==='uploaded');
  if(!reference)continue;
  if(reference.browser_download_url!==`https://github.com/${repository}/releases/download/${entry.tag_name}/source-references.json`||reference.size>256*1024||!/^sha256:[a-f0-9]{64}$/.test(reference.digest))throw Error('Invalid source binding');
  let bytes;
  if(process.env.GH_TOKEN){const response=await fetch(reference.browser_download_url,{credentials:'omit',signal:AbortSignal.timeout(30000)});if(!response.ok)throw Error('Source binding unavailable: '+entry.tag_name);bytes=Buffer.from(await response.arrayBuffer());}
  else bytes=cp.execFileSync('gh',['release','download',entry.tag_name,'--repo',repository,'--pattern','source-references.json','--output','-'],{windowsHide:true,timeout:45000});if(bytes.length!==reference.size||'sha256:'+crypto.createHash('sha256').update(bytes).digest('hex')!==reference.digest)throw Error('Source binding changed');
  const binding=JSON.parse(bytes.toString('utf8')),asset=entry.assets[0];
  if(binding.installer?.filename!==asset.name||binding.installer.bytes!==asset.size||binding.installer.sha256!==asset.digest.slice(7))throw Error('Installer binding mismatch');
  if(/^[a-f0-9]{64}$/.test(binding.licenseSha256??''))entry.licenseSha256=binding.licenseSha256;
  const historical=[],packs=binding.content?.packs??[];if(!Array.isArray(packs)||packs.length>32)throw Error('Invalid content binding');for(const pack of packs)contentPackVersion(pack,entry.tag_name.slice(1));
  for(const version of new Set(packs.map(p=>p.version).filter(Boolean))){
   const cached=releases.find(r=>r.tag_name==='v'+version);if(cached){historical.push(cached);continue;}
   const endpoint=`repos/${repository}/releases/tags/v${version}`;
   if(!/^\d+\.\d+\.\d+$/.test(version))throw Error('Invalid historical content version');
   if(process.env.GH_TOKEN){const response=await fetch('https://api.github.com/'+endpoint,{headers:{Authorization:`Bearer ${process.env.GH_TOKEN}`,Accept:'application/vnd.github+json'},signal:AbortSignal.timeout(30000)});if(!response.ok)throw Error('Historical content unavailable');historical.push(await response.json());}
   else historical.push(JSON.parse(cp.execFileSync('gh',['api',endpoint],{encoding:'utf8',windowsHide:true,timeout:45000})));
  }
  bindContent(entry,release,binding.content,repository,historical);
 }
 const feed={schema:1,releases:selected};fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output+'.tmp',JSON.stringify(feed,null,2)+'\n','utf8');fs.renameSync(output+'.tmp',output);console.log('Update feed: '+selected.length+' verified releases; newest '+selected[0].tag_name);
}
module.exports={entries,bindContent,generate,contentPackVersion,verifyContentReferences};
if(require.main===module)generate(process.argv[2]||process.env.GITHUB_REPOSITORY,process.argv[3]||'updates/windows-x64.json').catch(e=>{console.error(e.message);process.exitCode=1;});
