# Builds composition/index.html from the template: injects narration RMS data and the SFX clip list.
import json
tpl=open('work/index.template.html').read()
rms=json.load(open('work/rms.json'))
sfx=[]
def add(id,src,start,dur,vol,track):
    sfx.append(f'  <audio id="{id}" src="assets/sfx/{src}" data-start="{start:.2f}" data-duration="{dur}" data-track-index="{track}" data-volume="{vol}"></audio>')
# hook typing: thinned keypresses (every other character), alternating two tracks
keys=['keyboard/keypress-001.wav','keyboard/keypress-003.wav','keyboard/keypress-005.wav','keyboard/keypress-007.wav','keyboard/keypress-009.wav']
for n,i in enumerate(range(0,18,2)):
    add(f'key{n}',keys[n%5],0.45+i*0.065,0.2,0.45,11+n%2)
add('hit-reveal','impact/impactBell_heavy_000.ogg',4.0,2.5,0.5,13)       # beat-locked reveal
for n,at in enumerate([8.0,9.3,10.6]): add(f'tag{n}','interface/drop_001.ogg',at,0.6,0.55,14)
add('gen-click','interface/drop_002.ogg',11.7,0.6,0.5,14)
for n,at in enumerate([12.7,13.6,14.5]): add(f'bub{n}','interface/drop_002.ogg',at,0.6,0.45,15)
add('lang-land','impact/impactSoft_medium_001.ogg',17.55,1.0,0.6,13)
add('hit-logo','impact/impactBell_heavy_003.ogg',18.5,3.0,0.55,16)     # beat-locked logo
html=tpl.replace('__RMS__',json.dumps(rms)).replace('__SFX__','\n'.join(sfx)).replace('  let smooth = 0;\n','')
open('composition/index.html','w').write(html)
print('built',len(sfx),'sfx')
