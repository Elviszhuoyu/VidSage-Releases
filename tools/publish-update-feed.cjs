const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),cp=require('node:child_process');
function entries(releases,repository){
 const base=`https://github.com/${repository}/releases`;
 return releases.filter(r=>!r.draft&&/^v\d+\.\d+\.\d+$/.test(r.tag_name)).map(r=>{
  const version=r.tag_name.slice(1),name=`VidSage-${version}-win11-x64-Setup.exe`,asset=r.assets.find(a=>a.name===name&&a.state==='uploaded');
  if(r.html_url!==`${base}/tag/${r.tag_name}`||!asset||asset.browser_download_url!==`${base}/download/${r.tag_name}/${name}`||!/^sha256:[a-f0-9]{64}$/.test(asset.digest)||!Number.isSafeInteger(asset.size)||asset.size<=0)return null;
  return {tag_name:r.tag_name,draft:false,prerelease:r.prerelease,html_url:r.html_url,assets:[{name,state:'uploaded',browser_download_url:asset.browser_download_url,digest:asset.digest,size:asset.size}]};
 }).filter(Boolean).sort((a,b)=>{const x=a.tag_name.slice(1).split('.').map(Number),y=b.tag_name.slice(1).split('.').map(Number);return y[0]-x[0]||y[1]-x[1]||y[2]-x[2];}).slice(0,30);
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
 }
 const feed={schema:1,releases:selected};fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output+'.tmp',JSON.stringify(feed,null,2)+'\n','utf8');fs.renameSync(output+'.tmp',output);console.log('Update feed: '+selected.length+' verified releases; newest '+selected[0].tag_name);
}
module.exports={entries,generate};
if(require.main===module)generate(process.argv[2]||process.env.GITHUB_REPOSITORY,process.argv[3]||'updates/windows-x64.json').catch(e=>{console.error(e.message);process.exitCode=1;});
