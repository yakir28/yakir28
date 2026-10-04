# Builds composition/index.html from the v2 template: injects narration energy, word timings and the SFX clips.
import json
tpl=open('work/index.template.html').read()
rms=json.load(open('work/rms.json')); words=json.load(open('work/words.json'))
VO_AT=[0.35,3.65,6.3,10.6,13.85,16.75]
sfx=[]
def add(id,src,start,dur,vol,track):
    sfx.append(f'  <audio id="{id}" src="assets/sfx/{src}" data-start="{start:.2f}" data-duration="{dur}" data-track-index="{track}" data-volume="{vol}"></audio>')
keys=['keyboard/keypress-001.wav','keyboard/keypress-003.wav','keyboard/keypress-005.wav','keyboard/keypress-007.wav','keyboard/keypress-009.wav']
for n,w in enumerate(words[0]): add(f'key{n}',keys[n%5],VO_AT[0]+w['s'],0.2,0.4,11+n%2)      # silent words land like typed keys
add('hit-reveal','impact/impactBell_heavy_000.ogg',3.4,2.4,0.5,13)                            # beat-locked reveal
for k,at in enumerate([6.7,7.95,8.65]):
    for j in range(3): add(f'tag{k}{j}',keys[(k+j)%5],at+0.05+j*0.09,0.2,0.32,17+j)          # audio tag typing
for k,at in enumerate([7.03,8.25,8.92]): add(f'land{k}','interface/drop_001.ogg',at,0.6,0.5,14)
add('gen-click','interface/drop_002.ogg',9.75,0.6,0.5,15)
add('turn','interface/drop_002.ogg',11.95,0.6,0.4,15)
add('lang-land','impact/impactSoft_medium_001.ogg',14.95,1.0,0.6,13)
add('hit-logo','impact/impactBell_heavy_003.ogg',16.4,3.0,0.55,16)                            # beat-locked logo
html=tpl.replace('__RMS__',json.dumps(rms)).replace('__WORDS__',json.dumps(words)).replace('__SFX__','\n'.join(sfx))
open('composition/index.html','w').write(html); print('built',len(sfx),'sfx')
