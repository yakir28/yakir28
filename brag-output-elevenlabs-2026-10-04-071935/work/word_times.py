# Estimate word-level timings for each Kokoro narration clip (no ASR available offline):
# 1) find speech segments by energy (pauses Kokoro inserts at punctuation),
# 2) map punctuation-delimited phrases onto segments, 3) split each phrase by word length.
import numpy as np, json, re
from scipy.io import wavfile
LINES=["For a long time, words on a page stayed silent.","Then, they learned to speak.",
"Now, you can tell them how. Whisper it. Shout it. Laugh.","Cast a whole conversation, speaker by speaker.",
"In more than seventy languages.","ElevenLabs. Give your words a voice."]
out=[]
for i,line in enumerate(LINES,1):
    sr,x=wavfile.read(f'composition/assets/vo/vo{i}.wav');x=x.astype(float);x=x if x.ndim==1 else x.mean(1)
    hop=int(sr*.01);e=np.array([np.sqrt((x[k:k+hop]**2).mean()) for k in range(0,len(x)-hop,hop)])
    on=e>e.max()*0.06
    segs=[];k=0
    while k<len(on):
        if on[k]:
            j=k
            while j<len(on) and (on[j] or (j+8<len(on) and on[j:j+8].any())): j+=1
            segs.append([k/100,j/100]);k=j
        else:k+=1
    phrases=[p.strip() for p in re.split(r'(?<=[,.])\s+',line) if p.strip()]
    # merge segments down / or fall back to whole span
    if len(segs)!=len(phrases):
        # greedy merge closest gaps until counts match
        while len(segs)>len(phrases):
            gaps=[segs[n+1][0]-segs[n][1] for n in range(len(segs)-1)];n=int(np.argmin(gaps))
            segs[n]=[segs[n][0],segs[n+1][1]];del segs[n+1]
        if len(segs)<len(phrases):
            span=[segs[0][0],segs[-1][1]];tot=sum(len(p) for p in phrases);c=span[0];segs=[]
            for p in phrases:
                d=(span[1]-span[0])*len(p)/tot;segs.append([c,c+d]);c+=d
    # sanity: every phrase needs plausible speaking time (~45ms per char); else split the whole span by length
    if any((b-a)<0.045*len(p) for p,(a,b) in zip(phrases,segs)):
        span=[segs[0][0],max(q[1] for q in segs)];tot=sum(len(p) for p in phrases);c=span[0];segs=[]
        for p in phrases:
            d=(span[1]-span[0])*len(p)/tot;segs.append([c,c+d]);c+=d
    words=[]
    for p,(a,b) in zip(phrases,segs):
        ws=p.split();w=[len(re.sub(r'[^\w]','',q))+1.5 for q in ws];tot=sum(w);c=a
        for q,ww in zip(ws,w):
            d=(b-a)*ww/tot;words.append({"w":q,"s":round(c,3),"e":round(c+d,3)});c+=d
    out.append(words);print(i,[(q['w'],q['s']) for q in words])
json.dump(out,open('work/words.json','w'))
