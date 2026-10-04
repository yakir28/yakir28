import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR=48000; DUR=20.5; N=int(SR*DUR)
rng=np.random.default_rng(7)
L=np.zeros(N); R=np.zeros(N)
def f(n): return 440*2**((n-69)/12)
def lp(x,fc,o=2): return sosfilt(butter(o,fc,'low',fs=SR,output='sos'),x)
def hp(x,fc,o=2): return sosfilt(butter(o,fc,'high',fs=SR,output='sos'),x)
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],'band',fs=SR,output='sos'),x)
def add(sig,t,g=1.0,pan=0.0):
    i=int(t*SR); 
    if i>=N: return
    s=sig[:N-i]*g; L[i:i+len(s)]+=s*np.sqrt((1-pan)/2)*1.414/1.414; R[i:i+len(s)]+=s*np.sqrt((1+pan)/2)
def env(n,a,d):
    t=np.arange(n)/SR; return np.minimum(t/a if a>0 else 1,1)*np.exp(-t/d)
BEAT=0.5
# ---------- drums
def kick():
    n=int(.45*SR);t=np.arange(n)/SR
    fr=45+75*np.exp(-t/.04); ph=2*np.pi*np.cumsum(fr)/SR
    return np.sin(ph)*np.exp(-t/.16)*.9 + lp(rng.standard_normal(n),3000)*np.exp(-t/.004)*.15
def hat():
    n=int(.08*SR); return hp(rng.standard_normal(n),8000)*env(n,.0005,.018)*.18
def clap():
    n=int(.3*SR); x=bp(rng.standard_normal(n),900,4000); e=np.zeros(n);t=np.arange(n)/SR
    for o in (0,.011,.022): e+=(t>=o)*np.exp(-np.maximum(t-o,0)/(.012 if o<.02 else .09))
    return x*e*.22
K=kick();H=hat();C=clap()
kick_times=[]
for b in range(int(DUR/BEAT)):
    t=b*BEAT
    if t<3.0:
        if b%2==0 and t>0.3: add(K,t,.55); kick_times.append(t)   # half-time pulse in the hook
    elif t<20.0:
        add(K,t,.85); kick_times.append(t)
        add(H,t+BEAT/2,1,.25)
        if b%2==1: add(C,t,1,-.1)
        if 6<=t<17: add(H,t+BEAT*.75,.5,-.3)
add(K,20.0,.9); kick_times.append(20.0)
# ---------- harmony  (C - G - Am - F), bar = 2s
prog=[[48,64,67,72],[43,62,67,71],[45,64,69,72],[41,65,69,72]]
def saw(freq,n,detune=0):
    t=np.arange(n)/SR; out=0
    for d in (-detune,0,detune):
        ph=(t*freq*2**(d/1200))%1; out=out+(2*ph-1)
    return out/3
pad=np.zeros(N)
for bar in range(11):
    ch=prog[bar%4]; t0=bar*2.0; n=int(2.0*SR)
    if t0>=DUR: break
    seg=sum(saw(f(m),n,9) for m in ch[1:])/3
    e=np.minimum(np.arange(n)/SR/.08,1)*np.minimum((n-np.arange(n))/SR/.06,1)
    seg=seg*e
    i=int(t0*SR); pad[i:i+n]+=seg[:N-i]
cut=np.where(np.arange(N)/SR<3.0, 900, 2600)
pad=lp(pad,1800)*.10
pad=np.where(np.arange(N)/SR<3.0, lp(pad,700)*1.4, pad)
# sidechain duck
duck=np.ones(N)
for kt in kick_times:
    i=int(kt*SR); n=int(.35*SR); t=np.arange(n)/SR
    duck[i:i+n]=np.minimum(duck[i:i+n],1-.6*np.exp(-t/.09))
pad*=duck
# bass: eighth notes from 3.0
bass=np.zeros(N)
for k in range(int(3.0/.25),int(20.0/.25)):
    t=k*.25; root=prog[int(t//2)%4][0]; n=int(.23*SR); tt=np.arange(n)/SR
    s=np.sin(2*np.pi*f(root-12)*tt)+.35*np.sin(2*np.pi*f(root)*tt)
    s*=np.minimum(tt/.005,1)*np.exp(-tt/.12)
    i=int(t*SR); bass[i:i+n]+=s[:N-i]*(.32 if k%2 else .26)
bass*=duck**.5
# pluck arp 16ths from 6.0 to 17.0
def pluck(freq,dur=.25,g=.1):
    n=int(dur*SR);tt=np.arange(n)/SR
    s=np.sin(2*np.pi*freq*tt+1.2*np.exp(-tt/.03)*np.sin(2*np.pi*freq*2*tt))
    return s*np.minimum(tt/.002,1)*np.exp(-tt/.07)*g
arp=np.zeros(N)
for k in range(int(6/.125),int(17/.125)):
    t=k*.125; ch=prog[int(t//2)%4]; notes=[ch[1]+12,ch[2]+12,ch[3]+12,ch[2]+12]
    s=pluck(f(notes[k%4]),.2,.045 if k%2 else .06); i=int(t*SR); arp[i:i+len(s)]+=s[:N-i]
# ---------- sfx (in key)
def bell(freq,g):
    n=int(1.2*SR);tt=np.arange(n)/SR
    s=np.sin(2*np.pi*freq*tt+2.0*np.exp(-tt/.25)*np.sin(2*np.pi*freq*3.5*tt))
    return s*np.minimum(tt/.001,1)*np.exp(-tt/.35)*g
sfx=np.zeros(N)
def sadd(s,t,g=1):
    i=int(t*SR); sfx[i:i+len(s)]+=s[:N-i]*g
NT=[0.35,0.75,1.1,1.42,1.72,2.0]
for j,t in enumerate(NT):
    g=.11 if j==0 else .075
    sadd(bell(f(91),g),t); sadd(bell(f(96),g*1.1),t+.07)   # G6 -> C7 "ka-ching"
sadd(bell(f(84),.08),0.07); sadd(bell(f(91),.07),0.12)     # title slam
def whoosh(d=.45,lo=300,hi=5000,g=.18):
    n=int(d*SR); x=rng.standard_normal(n); out=np.zeros(n); blk=1024
    for s0 in range(0,n,blk):
        p=s0/n; fc=lo*(hi/lo)**p
        out[s0:s0+blk]=bp(x[s0:s0+blk+0],fc*.7,min(fc*1.4,20000))[:len(out[s0:s0+blk])]
    e=np.sin(np.pi*np.arange(n)/n)**2
    return lp(out*e,6000)*g
for t in (2.75,5.7,9.7,13.7,16.7): sadd(whoosh(),t)
for i in range(4): sadd(pluck(f([72,76,79,84][i]),.4,.09),10.75+i*.18)    # pills pop
sadd(pluck(f(84),.3,.08),8.62); sadd(pluck(f(88),.4,.1),8.74)               # click + added
sadd(pluck(f(79),.3,.06),15.6)
for k,t in enumerate([11.6,11.9,12.15,12.4,12.6,12.85,13.05,13.25,13.45,13.6]):
    sadd(pluck(f([84,88,91,86][k%4]),.25,.04),t+.45)                        # orders landing
sadd(pluck(f(84),.3,.09),19.0); sadd(bell(f(96),.06),19.08)                  # CTA click
# logo reveal shimmer
for i,m in enumerate([72,76,79,84]): sadd(bell(f(m+12),.035),3.15+i*.05)
# final chord ring at 20.0 (C)
n=int(.5*SR); fin=sum(saw(f(m),n,8) for m in [60,64,67,72])/4
fin=lp(fin*np.exp(-np.arange(n)/SR/.3),2500)*.15
sadd(fin,20.0)
# ---------- reverb send for sfx/arp
def reverb(x,dec=1.2,mix=.25):
    n=int(dec*SR); ir=rng.standard_normal(n)*np.exp(-np.arange(n)/SR/(dec/5)); ir=lp(ir,5000); ir/=np.sqrt((ir**2).sum())
    return x+fftconvolve(x,ir)[:len(x)]*mix
wet=reverb(sfx+arp*.8,1.4,.35)
mus=pad+bass
L+=mus+wet*.95+arp*.2; R+=mus+wet*1.05-arp*.0
# fade out tail
t=np.arange(N)/SR
fade=np.clip((DUR-t)/0.5,0,1); L*=fade; R*=fade
st=np.stack([L,R],1)
st=np.tanh(st*1.3)/1.3
st/=np.abs(st).max()/0.89
wavfile.write('audio.wav',SR,(st*32767).astype(np.int16))
print('ok',st.shape)
