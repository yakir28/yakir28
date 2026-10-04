s=open('monday.html').read()
def rep(a,b):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b)
# --- icons: add a few work-tool glyphs
rep('  <symbol id="hand"','''  <symbol id="i-grid" viewBox="0 0 64 64"><rect x="8" y="10" width="48" height="44" rx="6"/><path d="M8 24h48M8 38h48M24 10v44M40 10v44"/></symbol>
  <symbol id="i-doc" viewBox="0 0 64 64"><path d="M16 6h22l12 12v40H16zM38 6v12h12M24 32h18M24 42h18"/></symbol>
  <symbol id="i-check" viewBox="0 0 64 64"><rect x="8" y="8" width="48" height="48" rx="10"/><path d="M20 33l8 8 16-18"/></symbol>
  <symbol id="i-clock" viewBox="0 0 64 64"><circle cx="32" cy="32" r="24"/><path d="M32 18v15l10 6"/></symbol>
  <symbol id="i-kanban" viewBox="0 0 64 64"><rect x="6" y="8" width="14" height="40" rx="4"/><rect x="25" y="8" width="14" height="28" rx="4"/><rect x="44" y="8" width="14" height="48" rx="4"/></symbol>
  <symbol id="i-gantt" viewBox="0 0 64 64"><path d="M8 14h26M18 28h30M28 42h28M8 56h18"/></symbol>
  <symbol id="i-dash" viewBox="0 0 64 64"><circle cx="32" cy="34" r="22"/><path d="M32 12v22l16 14"/></symbol>
  <symbol id="hand"''')
rep(':root{--bg:#EDEFFA;--ink:#1B1D3A;--muted:#7C81A6;--green:#008060;--lime:#95BF47}',':root{--bg:#EDEFFA;--ink:#323338;--muted:#676879;--purple:#6161FF}')
rep('>Simplicity</div>','>Teamwork</div>')
rep("$('sw').style.background=k>.5?'#008060':'#D5D8EC';","$('sw').style.background=k>.5?'#6161FF':'#D5D8EC';")
# --- outro markup
i=s.index('<div class="abs" id="logo"'); j=s.index('<svg class="abs" id="handEl"')
s=s[:i]+'''<div class="abs" id="logo" style="left:0;right:0;top:690px;height:200px">
  <svg class="abs" style="left:390px;top:0;overflow:visible" width="300" height="180" viewBox="0 0 100 60">
    <line id="lred" x1="12" y1="48" x2="28" y2="14" stroke="#FF3D57" stroke-width="15" stroke-linecap="round"/>
    <line id="lyel" x1="40" y1="48" x2="56" y2="14" stroke="#FFCB00" stroke-width="15" stroke-linecap="round"/>
    <circle id="lgrn" cx="80" cy="44" r="8.5" fill="#00CA72"/>
  </svg>
</div>
<div class="abs" id="word" style="left:0;right:0;top:930px;text-align:center;font-weight:700;font-size:136px;letter-spacing:-.02em;color:var(--ink)"></div>
<div class="abs hl" id="url" style="top:1140px;font-size:46px;font-weight:600;color:var(--muted)">Work management for every team</div>
<div class="abs" id="cta" style="left:280px;top:1270px;width:520px;height:124px;border-radius:62px;background:var(--purple);color:#fff;font-weight:600;font-size:46px;display:flex;align-items:center;justify-content:center;gap:16px;box-shadow:0 20px 50px rgba(97,97,255,.4)">Get Started <span style="font-size:44px">→</span></div>
<div class="abs hl" id="fine" style="top:1430px;font-size:32px;font-weight:500;color:var(--muted)">Free forever. No credit card needed.</div>

'''+s[j:]
# --- data + view builders (BUBS .. end of body())
i=s.index('const BUBS='); j=s.index('const winEls=')
s=s[:i]+r'''const BUBS=[['i-grid','#00C875',210,430,1.0],['i-mail','#579BFC',560,330,1.1],['i-chat','#A25DDC',880,470,.9],['i-doc','#579BFC',150,720,.85],
            ['i-cal','#FF3D57',935,730,1.05],['i-check','#00C875',190,1180,1.1],['i-clock','#FDAB3D',890,1190,.95],['i-chart','#6161FF',360,1420,.9],
            ['i-receipt','#FF7575',720,1440,1.15],['i-kanban','#FDAB3D',540,1660,.8]];
const bubEls=BUBS.map(b=>{const d=document.createElement('div');d.className='abs bub';d.innerHTML=`<svg style="stroke:${b[1]}"><use href="#${b[0]}"/></svg>`;$('bubs').appendChild(d);return d});
// ---------- hook text (typed)
const HOOK=['Forget switching','between tools!'];
// ---------- views (monday status colors)
const ST={done:['Done','#00C875'],work:['Working on it','#FDAB3D'],stuck:['Stuck','#E2445C']};
const VIEWS=[
 {name:'Main Table',color:'#6161FF',tint:'#ECECFF',icon:'i-grid',head:'Plan every project.'},
 {name:'Kanban',color:'#FDAB3D',tint:'#FFF2DE',icon:'i-kanban',head:'Move work forward.'},
 {name:'Timeline',color:'#579BFC',tint:'#E6F0FF',icon:'i-gantt',head:'See every deadline.'},
 {name:'Calendar',color:'#00C875',tint:'#DFF8EC',icon:'i-cal',head:'Never miss a date.'},
 {name:'Dashboard',color:'#E2445C',tint:'#FDE6EA',icon:'i-dash',head:'Track it all in one place.'},
];
const VT=[5.0,7.0,9.0,11.0,13.0]; // view start times
const NAVS=['Home','My work','Q4 Launch','Content plan','Sprints','Dashboards'];
const PEOPLE=[['Ava Martin','AM','#FDAB3D'],['Liam Chen','LC','#579BFC'],['Noah Patel','NP','#00C875'],['Mia Rossi','MR','#FF5AC4'],['Leo Garcia','LG','#A25DDC'],['Zoe Kim','ZK','#E2445C']];
const TASKS=[['Finalize launch plan',0,'done','Oct 6'],['Write release notes',1,'work','Oct 9'],['Design landing page',3,'stuck','Oct 12'],['QA mobile app',2,'work','Oct 14'],['Press outreach',4,'done','Oct 16'],['Launch webinar',5,'work','Oct 20']];
const av=(p,sz=44)=>`<div class="av" style="width:${sz}px;height:${sz}px;font-size:${sz*.36}px;background:${PEOPLE[p][2]}">${PEOPLE[p][1]}</div>`;
const pill=(k,cls='')=>`<span class="${cls}" style="display:inline-flex;align-items:center;justify-content:center;width:150px;height:40px;border-radius:6px;background:${ST[k][1]};color:#fff;font-size:17px;font-weight:600">${ST[k][0]}</span>`;
function shell(v){
  return `<div class="abs hdr" style="background:${v.color}"><svg width="54" height="32" viewBox="0 0 100 60"><line x1="12" y1="48" x2="28" y2="14" stroke="#fff" stroke-width="15" stroke-linecap="round"/><line x1="40" y1="48" x2="56" y2="14" stroke="#fff" stroke-width="15" stroke-linecap="round"/><circle cx="80" cy="44" r="8.5" fill="#fff"/></svg>Marketing<div class="search">Search</div>${av(4,44).replace('class="av"','class="av" style="border:3px solid rgba(255,255,255,.6)"')}</div>
  <div class="abs side">${NAVS.map((n,i)=>`<div class="nav" style="${i===2?`background:${v.tint};color:${v.color}`:''}"><i style="${i===2?`background:${v.color}`:''}"></i>${n}</div>`).join('')}</div>
  <div class="abs main"><div class="h2">Q4 Product Launch</div>
   <div style="display:flex;gap:20px;margin:12px 0 18px;border-bottom:2px solid #EEF0F6;font-size:17px;font-weight:600;color:#888">${VIEWS.map(w=>`<span style="padding:6px 0 10px;${w===v?`color:${v.color};border-bottom:4px solid ${v.color};margin-bottom:-2px`:''}">${w.name}</span>`).join('')}</div>
   ${body(v)}</div>`;
}
function body(v){
  if(v.name==='Main Table') return `
   <div class="b" style="display:flex;align-items:center;gap:10px;font-weight:700;font-size:21px;color:${v.color};margin-bottom:6px">▾ This sprint</div>
   <div class="row" style="height:42px;font-size:16px;color:#999;font-weight:600;border-left:6px solid ${v.color};padding-left:12px"><span style="width:230px">Task</span><span style="width:60px">Owner</span><span style="width:150px;text-align:center">Status</span><span>Due</span></div>
   ${TASKS.map((x,i)=>`<div class="row b" style="height:76px;font-size:19px;border-left:6px solid ${v.color};padding-left:12px"><span style="width:230px">${x[0]}</span><span style="width:60px">${av(x[1],42)}</span>${pill(x[2],i===2?'flip':'')}<span style="color:#777;font-size:17px">${x[3]}</span></div>`).join('')}`;
  if(v.name==='Kanban') return `
   <div style="display:flex;gap:14px;position:relative">${['work','stuck','done'].map(k=>`
    <div class="b" style="flex:1;border-radius:14px;background:#F5F6F8;padding:0 0 12px;min-height:600px">
     <div style="height:48px;border-radius:14px 14px 0 0;background:${ST[k][1]};color:#fff;font-weight:600;font-size:18px;display:flex;align-items:center;padding:0 14px">${ST[k][0]}</div>
     ${TASKS.filter(x=>x[2]===k).map(x=>`<div style="margin:12px 10px 0;background:#fff;border-radius:10px;padding:14px;box-shadow:0 2px 6px rgba(0,0,0,.06);font-size:17px;font-weight:600;line-height:1.3">${x[0]}<div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px;color:#999;font-weight:500;font-size:15px">${x[3]}${av(x[1],34)}</div></div>`).join('')}
    </div>`).join('')}
    <div class="mover abs" style="left:10px;top:${48+12+2*(108+12)}px;width:183px;background:#fff;border-radius:10px;padding:14px;box-shadow:0 14px 30px rgba(0,0,0,.18);font-size:17px;font-weight:600;line-height:1.3;border-left:5px solid #FDAB3D">QA mobile app<div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px;color:#999;font-weight:500;font-size:15px">Oct 14${av(2,34)}</div></div>
   </div>`;
  if(v.name==='Timeline') return `
   <div style="display:flex;font-size:16px;color:#999;font-weight:600;margin-left:190px;border-bottom:2px solid #F0F1F7;padding-bottom:8px">${['Oct','Nov','Dec'].map(m=>`<span style="flex:1">${m}</span>`).join('')}</div>
   <div style="position:relative">
   ${TASKS.map((x,i)=>{const s0=[0,.12,.25,.4,.52,.68][i],w=[.22,.25,.3,.24,.3,.28][i];return `<div class="row b" style="height:80px;font-size:17px"><span style="width:180px;line-height:1.2">${x[0]}</span><div style="flex:1;position:relative;height:44px"><div class="gbar abs" data-w="${w}" style="left:${s0*100}%;top:0;height:44px;width:0;border-radius:22px;background:${['#579BFC','#A25DDC','#FDAB3D','#00C875','#FF5AC4','#579BFC'][i]};display:flex;align-items:center;justify-content:flex-end;padding-right:4px;overflow:hidden">${av(x[1],36)}</div></div></div>`}).join('')}
   <div class="today abs" style="left:${190+0.45*440}px;top:0;bottom:0;width:3px;background:#E2445C"></div></div>`;
  if(v.name==='Calendar'){
   const ev={2:['Kickoff','#6161FF'],6:['Release notes','#FDAB3D'],9:['Design review','#A25DDC'],12:['QA sprint','#00C875'],15:['Press day','#FF5AC4'],18:['Webinar','#579BFC'],23:['Retro','#E2445C']};
   return `<div style="display:flex;justify-content:space-between;font-weight:700;font-size:21px;margin-bottom:10px">October 2026<span style="color:#999;font-weight:500;font-size:17px">Month</span></div>
   <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px;font-size:15px;color:#999;font-weight:600;margin-bottom:6px">${['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].map(d=>`<span>${d}</span>`).join('')}</div>
   <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px">${[...Array(28)].map((_,i)=>`<div style="height:108px;border-radius:10px;background:#F7F8FC;padding:6px;font-size:15px;color:#777;font-weight:600">${i+1}${ev[i]?`<div class="ev" style="margin-top:6px;border-radius:6px;padding:4px 5px;background:${ev[i][1]};color:#fff;font-size:12px;font-weight:600;line-height:1.15">${ev[i][0]}</div>`:''}</div>`).join('')}</div>`;}
  if(v.name==='Dashboard') return `
   <div style="display:flex;gap:14px">${[['Tasks done','128','k1'],['On track','92%','k2'],['Overdue','3','k3']].map(k=>`
     <div class="b" style="flex:1;border-radius:16px;background:${v.tint};padding:16px"><div style="font-size:16px;color:#777;font-weight:600">${k[0]}</div><div id="${k[2]}" style="margin-top:4px;font-weight:700;font-size:34px;color:${k[2]==='k3'?'#E2445C':'#323338'}">${k[1]}</div></div>`).join('')}</div>
   <div style="display:flex;gap:14px;margin-top:16px">
    <div class="b" style="width:250px;height:420px;border-radius:16px;border:2px solid #F0F1F7;padding:16px;position:relative">
      <div style="font-weight:700;font-size:18px">Status</div>
      <div id="donut" class="abs" style="left:35px;top:70px;width:180px;height:180px;border-radius:50%"></div>
      <div class="abs" style="left:80px;top:115px;width:90px;height:90px;border-radius:50%;background:#fff"></div>
      <div class="abs" style="left:18px;top:285px;font-size:15px;line-height:1.9;font-weight:600;color:#555">${['done','work','stuck'].map(k=>`<div><b style="display:inline-block;width:12px;height:12px;border-radius:3px;background:${ST[k][1]};margin-right:8px"></b>${ST[k][0]}</div>`).join('')}</div>
    </div>
    <div class="b" style="flex:1;height:420px;border-radius:16px;border:2px solid #F0F1F7;padding:16px;position:relative">
      <div style="font-weight:700;font-size:18px">Done per week</div>
      <div class="abs" style="left:20px;right:20px;bottom:46px;height:300px;display:flex;align-items:flex-end;gap:14px">${[.3,.45,.4,.6,.72,.95].map((h,i)=>`<div class="vbar" data-h="${h}" style="flex:1;height:0;border-radius:8px 8px 3px 3px;background:${i===5?'#00C875':'#BDEFD7'}"></div>`).join('')}</div>
      <div class="abs" style="left:20px;right:20px;bottom:14px;display:flex;gap:14px;font-size:14px;color:#999;font-weight:600">${['W1','W2','W3','W4','W5','W6'].map(d=>`<span style="flex:1;text-align:center">${d}</span>`).join('')}</div>
    </div></div>`;
}
'''+s[j:]
# floaters: teammates with status chips
rep("const FL=[[0,130,620,'+ $48.00'],[3,950,880,'+ $126.50'],[1,110,1260,'+ $215.00']];","const FL=[[0,130,640,'✓ Done'],[3,950,900,'@mentioned you'],[1,110,1260,'✓ Approved']];")
rep("background:#fff;color:#0C5132;box-shadow","background:#fff;color:#323338;box-shadow")
# view-specific animation
i=s.index("    if(v.name==='Orders')"); j=s.index("  });\n  // headline + tab")
s=s[:i]+r'''    if(v.name==='Main Table'){const fl=w.querySelector('.flip');const d=lt>1.25;fl.textContent=d?'Done':'Stuck';fl.style.background=d?'#00C875':'#E2445C';fl.style.transform=`scale(${1+(seg(lt,1.25,1.35)-seg(lt,1.35,1.55))*.15})`}
    if(v.name==='Kanban'){const m=w.querySelector('.mover');const q=eio(seg(lt,.75,1.35));const lift=seg(lt,.6,.75)-seg(lt,1.35,1.5);
      m.style.transform=`translate(${q*2*(183+14+14/3)}px,${q*-240+(-lift*10)}px) rotate(${Math.sin(q*Math.PI)*4}deg)`;m.style.opacity=clamp(seg(lt,.35,.6));m.style.borderLeftColor=q>.5?'#00C875':'#FDAB3D';}
    if(v.name==='Timeline'){w.querySelectorAll('.gbar').forEach((b,j)=>{b.style.width=(eio(seg(lt,.35+j*.1,1.0+j*.1))*b.dataset.w*100)+'%'});}
    if(v.name==='Calendar'){w.querySelectorAll('.ev').forEach((e,j)=>{const p=popv(lt,.4+j*.1,.35);e.style.transform=`scale(${p})`;e.style.opacity=clamp(p*2)});}
    if(v.name==='Dashboard'){const k=eo(seg(lt,.4,1.4));$('k1').textContent=Math.round(128*k);$('k2').textContent=Math.round(92*k)+'%';$('k3').textContent=Math.round(3*k);
      const d=eio(seg(lt,.4,1.3))*360;$('donut').style.background=`conic-gradient(#00C875 0 ${Math.min(d,223)}deg,#FDAB3D ${Math.min(d,223)}deg ${Math.min(d,324)}deg,#E2445C ${Math.min(d,324)}deg ${d}deg,#EEF0F6 ${d}deg 360deg)`;}
'''+s[j:]
rep("w.querySelectorAll('.bar').forEach((b,j)=>{b.style.width=(eio(seg(lt,.5+j*.08,1.2+j*.08))*b.dataset.w*100)+'%'});\n","")
# outro animation
rep("$('lbody').style.transform=`translate(${(1-a)*-260}px,${(1-a)*120}px) rotate(${(1-a)*-40}deg)`;$('lbody').style.opacity=a;",
    "for(const [id,p,dx,dy] of [['lred',a,-40,30],['lyel',b,30,-40]]){const e=$(id);e.style.transform=`translate(${(1-p)*dx}px,${(1-p)*dy}px)`;e.style.opacity=p;e.style.transformBox='fill-box';e.style.transformOrigin='50% 50%';}")
rep("$('lhandle').style.transform=`translate(${(1-b)*240}px,${(1-b)*-160}px) rotate(${(1-b)*60}deg)`;$('lhandle').style.opacity=b;","")
rep("$('lshine').style.transform=`scale(${c2<=0?0:lerp(.3,1,c2)})`;$('lshine').style.opacity=c2;",
    "{const g=$('lgrn');g.style.transformBox='fill-box';g.style.transformOrigin='50% 50%';g.style.transform=`scale(${popv(t,15.75,.4)})`;}")
rep("$('word').innerHTML=[...'shopify'].map(c=>`<span style=\"display:inline-block\">${c}</span>`).join('');",
    "$('word').innerHTML=[...'monday.com'].map((c,i)=>`<span style=\"display:inline-block;${i>=6?'font-weight:400':''}\">${c}</span>`).join('');")
rep("letters.forEach((l,i)=>{const p=eo(seg(t,16.0+i*.05,16.45+i*.05));l.style.opacity=p;l.style.transform=`translateX(${(i-3)*(1-p)*60}px)`});",
    "letters.forEach((l,i)=>{const p=eo(seg(t,16.0+i*.04,16.45+i*.04));l.style.opacity=p;l.style.transform=`translateX(${(i-4.5)*(1-p)*50}px)`});")
rep("rise($('url'),t,16.45,.45,30);","rise($('url'),t,16.45,.45,30);rise($('fine'),t,17.0,.45,20);")
rep("['logo','word','url','cta'].forEach(","['logo','word','url','cta','fine'].forEach(")
rep("0 20px 50px rgba(0,128,96,.35),0 0 0 ${g*34}px rgba(0,128,96,${.3*(1-g)})","0 20px 50px rgba(97,97,255,.4),0 0 0 ${g*34}px rgba(97,97,255,${.3*(1-g)})")
rep("x=lerp(1200,690,m);y=lerp(2050,1392,m)","x=lerp(1200,700,m);y=lerp(2050,1360,m)")
open('monday.html','w').write(s)
print('ok')
