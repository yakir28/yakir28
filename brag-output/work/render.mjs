import { chromium } from 'playwright';
import { spawn } from 'child_process';
import path from 'path';
const FPS=30, DUR=20.5, N=Math.round(FPS*DUR);
const ff = spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','medium','silent.mp4'],{stdio:['pipe','inherit','inherit']});
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1080,height:1920} });
await p.goto('file://'+path.resolve('composition.html'));
await p.evaluate(()=>window.ready);
for(let i=0;i<N;i++){
  await p.evaluate(t=>window.render(t), i/FPS);
  const buf = await p.screenshot({type:'jpeg',quality:95});
  if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
  if(i%100===0) console.log('frame',i,'/',N);
}
ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close();
