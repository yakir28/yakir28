# Original cinematic score for the ElevenLabs brag (v2, 20.0s). D minor, 120 BPM grid anchored at 3.4s.
# Hits land on the cuts: braam at 3.4 (reveal), riser into the logo hit at 16.4; swooshes on every scene change.
import numpy as np, sys
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR=48000; DUR=20.0; H1=3.4; H2=16.4; N=int(SR*DUR); rng=np.random.default_rng(3)
t=np.arange(N)/SR
f=lambda n:440*2**((n-69)/12)
lp=lambda x,fc,o=2:sosfilt(butter(o,fc,'low',fs=SR,output='sos'),x)
hp=lambda x,fc,o=2:sosfilt(butter(o,fc,'high',fs=SR,output='sos'),x)
bp=lambda x,lo,hi:sosfilt(butter(2,[lo,hi],'band',fs=SR,output='sos'),x)
L=np.zeros(N);R=np.zeros(N)
def put(sig,at,g=1.0,pan=0.0):
    i=int(at*SR)
    if i>=N:return
    s=sig[:N-i]*g;L[i:i+len(s)]+=s*(1-max(pan,0));R[i:i+len(s)]+=s*(1+min(pan,0))
def saw(fr,n,det=0):
    tt=np.arange(n)/SR;return sum(2*((tt*fr*2**(d/1200))%1)-1 for d in (-det,0,det))/3
def env_ad(n,a,d):
    tt=np.arange(n)/SR;return np.minimum(tt/max(a,1e-4),1)*np.exp(-tt/d)
# --- drone (whole piece), opens up after the reveal
n=N; dr=(saw(f(38),n,7)+saw(f(45),n,5))*0.5
cut=np.interp(t,[0,H1-.1,H1,6.5,H2-.1,H2,DUR],[180,700,1400,900,1100,2200,600])
# time-varying lowpass via blocks
out=np.zeros(N);blk=2400
for s0 in range(0,N,blk):
    out[s0:s0+blk]=lp(dr[max(0,s0-blk*4):s0+blk],cut[s0])[-len(dr[s0:s0+blk]):]
drone=out*np.interp(t,[0,1.2,H1-.1,H1,H2,DUR-1,DUR],[0,.10,.16,.12,.14,.06,0])
put(drone,0,1)
# --- heartbeat sub pulses in the hook
def thump(fr=55,g=1):
    m=int(.35*SR);tt=np.arange(m)/SR;return np.sin(2*np.pi*np.cumsum(fr*(1+1.5*np.exp(-tt/.03)))/SR)*np.exp(-tt/.12)*g
for k,b in enumerate([0.4,1.25,2.1,2.75]):
    put(thump(50,.5+.12*k),b);put(thump(50,.35+.1*k),b+.22)
# --- riser into the reveal and into the logo
def riser(d,g):
    m=int(d*SR);x=rng.standard_normal(m);o=np.zeros(m);b=1024
    for s0 in range(0,m,b):
        fc=300*(9000/300)**(s0/m);o[s0:s0+b]=bp(x[s0:s0+b],fc*.6,min(fc*1.5,20000))
    tt=np.arange(m)/SR;tone=np.sin(2*np.pi*np.cumsum(np.linspace(f(50),f(74),m))/SR)*.3
    return (o+tone)*(tt/d)**2.2*g
put(riser(1.1,.22),H1-1.1);put(riser(1.4,.24),H2-1.4)
# swooshes on scene changes
for at in (6.0,10.4,13.6):
    m=int(.7*SR);x=bp(rng.standard_normal(m),400,5000);tt=np.arange(m)/SR;put(x*np.sin(np.pi*tt/.7)**2*.10,at-.35)
# --- braam hits
def braam(root,d,g):
    m=int(d*SR);tt=np.arange(m)/SR
    s=sum(saw(f(n),m,12) for n in (root-12,root,root+7,root+12))/4
    s=lp(s,1600)*np.minimum(tt/.02,1)*np.exp(-tt/1.1)
    sub=np.sin(2*np.pi*f(root-24)*tt)*np.exp(-tt/.9)*.8
    boom=lp(rng.standard_normal(m),180)*np.exp(-tt/.25)*1.5
    return (s+sub+boom)*g
put(braam(50,3.4,.5),H1)           # beat-locked: reveal
put(braam(50,3.6,.6),H2)           # beat-locked: logo
# --- warm pad after reveal: Dm - Bb - F - C (2s bars from 4.0)
prog=[[50,53,57],[46,50,53],[53,57,60],[48,52,55]]
for bar in range(8):
    t0=H1+bar*2
    if t0>=H2:break
    m=int(2.05*SR);tt=np.arange(m)/SR
    pad=sum(np.sin(2*np.pi*f(n+12)*tt+.4*np.sin(2*np.pi*.25*tt)) for n in prog[bar%4])/3
    pad*=np.minimum(tt/.4,1)*np.minimum((2.05-tt)/.3,1)
    put(pad,t0,.07,(-.2 if bar%2 else .2))
# --- piano/pluck ostinato 8ths from 7.5 (scene 3) to 18.5
def pluck(fr,g):
    m=int(.6*SR);tt=np.arange(m)/SR
    s=np.sin(2*np.pi*fr*tt+.9*np.exp(-tt/.15)*np.sin(2*np.pi*fr*2*tt))+.2*np.sin(2*np.pi*fr*3*tt)*np.exp(-tt/.08)
    return s*np.minimum(tt/.003,1)*np.exp(-tt/.35)*g
for k in range(int((H2-6.15)/.25)):
    at=6.15+k*.25;ch=prog[int((at-H1)//2)%4];notes=[ch[0]+24,ch[1]+24,ch[2]+24,ch[1]+24]
    put(pluck(f(notes[k%4]),.05 if k%2 else .065),at,1,(.3 if k%2 else -.3))
# --- low pulse (toms) from 12.4, builds
for k in range(int((H2-10.65)/.5)):
    at=10.65+k*.5;put(thump(70,.18+.02*k),at)
# --- final chord rings over the logo (D major lift)
m=int(3.6*SR);tt=np.arange(m)/SR
fin=sum(np.sin(2*np.pi*f(n)*tt)*np.exp(-tt/(1.8)) for n in (62,66,69,74,78))/5
put(fin,H2,.18)
# --- space
def reverb(x,dec=2.4,mix=.35):
    m=int(dec*SR);ir=lp(rng.standard_normal(m)*np.exp(-np.arange(m)/SR/(dec/6)),6000);ir/=np.sqrt((ir**2).sum())
    return x+fftconvolve(x,ir)[:len(x)]*mix
L=reverb(L);R=reverb(R)
fade=np.clip((DUR-t)/0.8,0,1);L*=fade;R*=fade
st=np.stack([L,R],1);st=np.tanh(st*1.1)/1.1;st/=np.abs(st).max()/.89
wavfile.write(sys.argv[1],SR,(st*32767).astype(np.int16));print('score ok')
