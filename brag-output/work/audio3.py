# Soundtrack for the explainer-style cut: bright 120 BPM corporate-pop, sfx in key (C major).
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR=48000; DUR=19.0; N=int(SR*DUR)
rng=np.random.default_rng(11)
def f(n): return 440*2**((n-69)/12)
def lp(x,fc,o=2): return sosfilt(butter(o,fc,'low',fs=SR,output='sos'),x)
def hp(x,fc,o=2): return sosfilt(butter(o,fc,'high',fs=SR,output='sos'),x)
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],'band',fs=SR,output='sos'),x)
tracks={k:np.zeros(N) for k in ('drum','bass','pad','keys','sfx')}
def put(name,sig,t,g=1.0):
    i=int(t*SR)
    if i>=N or i<0: return
    s=sig[:N-i]*g; tracks[name][i:i+len(s)]+=s
# drums
def kick():
    n=int(.4*SR);t=np.arange(n)/SR;fr=48+80*np.exp(-t/.035)
    return np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-t/.14)*.85+lp(rng.standard_normal(n),3500)*np.exp(-t/.004)*.12
def hat(d=.018):
    n=int(.08*SR);t=np.arange(n)/SR;return hp(rng.standard_normal(n),8000)*np.exp(-t/d)*.16
def clap():
    n=int(.3*SR);t=np.arange(n)/SR;e=sum((t>=o)*np.exp(-np.maximum(t-o,0)/(.012 if o<.02 else .1)) for o in (0,.01,.021))
    return bp(rng.standard_normal(n),1000,5000)*e*.2
def snap():
    n=int(.12*SR);t=np.arange(n)/SR;return bp(rng.standard_normal(n),1800,6000)*np.exp(-t/.02)*.22
K,H,C,SN=kick(),hat(),clap(),snap()
kicks=[]
for b in range(int(18.0/.5)):
    t=b*.5
    if t<1.0: continue
    if t<5.0:   # build: snaps on 2&4, soft kick on 1&3, hats
        if b%2==0: put('drum',K,t,.6); kicks.append(t)
        else: put('drum',SN,t,.8)
        put('drum',H,t+.25,.7)
    else:
        put('drum',K,t,.85); kicks.append(t)
        put('drum',H,t+.25); put('drum',hat(.01),t+.125,.35); put('drum',hat(.01),t+.375,.35)
        if b%2==1: put('drum',C,t)
put('drum',K,18.0,.9); kicks.append(18.0)
# fill into the drop
for k in range(8): put('drum',SN,4.5+k*.0625,.25+.08*k)
# harmony: C - Am - F - G per 2s bar
prog=[[48,60,64,67],[45,60,64,69],[41,60,65,69],[43,59,62,67]]
def keytone(freq,dur,g):  # electric-piano-ish
    n=int(dur*SR);t=np.arange(n)/SR
    s=np.sin(2*np.pi*freq*t+.8*np.exp(-t/.4)*np.sin(2*np.pi*freq*t))+.25*np.sin(4*np.pi*freq*t)*np.exp(-t/.15)
    return s*np.minimum(t/.004,1)*np.exp(-t/.6)*g
for bar in range(10):
    t0=bar*2.0
    if t0>=18: break
    ch=prog[bar%4]
    # pad
    n=int(2*SR);tt=np.arange(n)/SR
    pad=sum(np.sin(2*np.pi*f(m+12)*tt+np.sin(2*np.pi*.3*tt)*.3) for m in ch[1:])/3
    pad*=np.minimum(tt/.15,1)*np.minimum((2-tt)/.1,1)
    put('pad',pad,t0,.10 if t0>=4 else .08)
    if t0>=1.0 or bar==0:
        # keys: syncopated stabs (on 1, &2, 4)
        for off in ((0,.5,1.25) if t0<5 else (0,.5,.75,1.25,1.5)):
            for m in ch[1:]: put('keys',keytone(f(m+12),.5,.05),t0+off)
    if t0>=4.0:
        for k in range(8):
            t=t0+k*.25; n=int(.22*SR);tt=np.arange(n)/SR
            s=(np.sin(2*np.pi*f(ch[0]-12)*tt)+.4*np.sin(2*np.pi*f(ch[0])*tt))*np.minimum(tt/.004,1)*np.exp(-tt/.1)
            put('bass',s,t,.3 if t>=5 else .2)
# final chord
for m in [48,60,64,67,72,76]: put('keys',keytone(f(m),1.0,.07),18.0)
# ---------- sfx
def pop(freq,g=.1,d=.06):
    n=int(.25*SR);t=np.arange(n)/SR
    fr=freq*(1+1.2*np.exp(-t/.012));return np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-t/d)*g
def tick(g=.05):
    n=int(.03*SR);t=np.arange(n)/SR;return bp(rng.standard_normal(n),2500,7000)*np.exp(-t/.004)*g
def whoosh(d=.5,lo=300,hi=6000,g=.14):
    n=int(d*SR);x=rng.standard_normal(n);out=np.zeros(n);blk=1024
    for s0 in range(0,n,blk):
        fc=lo*(hi/lo)**(s0/n);out[s0:s0+blk]=bp(x[s0:s0+blk],fc*.7,min(fc*1.4,20000))
    return lp(out*np.sin(np.pi*np.arange(n)/n)**2,7000)*g
def bell(freq,g):
    n=int(1.0*SR);t=np.arange(n)/SR
    return np.sin(2*np.pi*freq*t+1.6*np.exp(-t/.2)*np.sin(2*np.pi*freq*3.5*t))*np.exp(-t/.3)*g
scale=[72,74,76,79,81,84,86,88,91,93]
for i in range(10): put('sfx',pop(f(scale[i]),.07),.15+i*.09)              # bubbles pop in
for j in range(37): put('sfx',tick(.04),1.0+j*.8/37)                           # typing
put('sfx',pop(f(79),.09),3.55)                                                  # toggle appears
put('sfx',tick(.12),3.95); put('sfx',bell(f(84),.06),4.0)                       # toggle click
put('sfx',whoosh(.5,2000,200,.16),4.15)                                         # bubbles sucked in
put('sfx',pop(f(72),.12,.09),4.6); put('sfx',bell(f(88),.05),4.62)             # window lands
for k in range(5): put('sfx',pop(f(76+k*2 if k<3 else 79+k),.05),4.9+k*.07)    # nav buttons
for i in range(3): put('sfx',pop(f([84,88,91][i]),.08),5.55+i*.25)              # avatars
for T in (7.0,9.0,11.0,13.0):
    put('sfx',tick(.14),T-.15); put('sfx',pop(f(84),.06,.04),T-.14)             # tap
    put('sfx',whoosh(.45,400,5000,.12),T-.05)                                   # slide
put('sfx',bell(f(88),.045),6.25); put('sfx',pop(f(79),.05),7.85); put('sfx',pop(f(84),.07),8.35)  # status flip, card lift + drop
for j in range(7): put('sfx',pop(f(scale[j]),.03),11.4+j*.1)   # calendar events
put('sfx',whoosh(.6,300,7000,.16),14.8)                                         # outro sweep
put('sfx',pop(f(67),.1,.08),15.6); put('sfx',pop(f(72),.1,.08),15.75)          # logo pieces
for i,m in enumerate([84,88,91,96]): put('sfx',bell(f(m),.035),15.9+i*.05)      # sparkle
put('sfx',pop(f(79),.1),16.7)                                                   # CTA
put('sfx',tick(.15),17.79); put('sfx',bell(f(91),.06),17.82)                    # click
# ---------- mix
def reverb(x,dec=1.3,mix=.3):
    n=int(dec*SR);ir=lp(rng.standard_normal(n)*np.exp(-np.arange(n)/SR/(dec/5)),5000);ir/=np.sqrt((ir**2).sum())
    return x+fftconvolve(x,ir)[:len(x)]*mix
duck=np.ones(N)
for kt in kicks:
    i=int(kt*SR);n=int(.3*SR);tt=np.arange(n)/SR;duck[i:i+n]=np.minimum(duck[i:i+n][:len(tt[:N-i])],(1-.5*np.exp(-tt/.08))[:N-i])
keys=reverb(lp(tracks['keys'],5000),1.2,.25)*duck**.6
pad=lp(tracks['pad'],2500)*duck
sfx=reverb(tracks['sfx'],1.4,.3)
bass=tracks['bass']*duck**.5
L=tracks['drum']+bass+pad*1.0+keys*1.05+sfx*.95
R=tracks['drum']+bass+pad*1.0+keys*.95+sfx*1.05
# drums and bass stop after final hit; tail fade
t=np.arange(N)/SR;fade=np.clip((DUR-t)/0.8,0,1);L*=fade;R*=fade
st=np.tanh(np.stack([L,R],1)*1.2)/1.2;st/=np.abs(st).max()/.89
wavfile.write('audio3.wav',SR,(st*32767).astype(np.int16));print('ok')
