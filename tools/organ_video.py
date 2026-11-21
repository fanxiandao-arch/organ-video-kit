#!/usr/bin/env python3
"""Organ first-person cinematic video pipeline.
Usage: python3 organ_video.py EP_DIR/episode.json {tts|preview|render|all} [--hd]
EP_DIR must contain img/<key>.png for every image key used in lines."""
import json,sys,os,io,glob,base64,asyncio,subprocess
from PIL import Image
CHROME=os.environ.get("CHROME") or next(iter(glob.glob("/opt/.devin/chrome/chrome/*/chrome-linux64/chrome")),None)
FPS=15
LIB=os.environ.get("ORGAN_LIB") or os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","library")
HTML=r"""<!doctype html><html><body style="margin:0"><canvas id="c"></canvas><script>
const EP=__EP__,TL=__TL__,IMS=__IMS__,K=__K__;const W=540,H=960,F='"Noto Sans CJK SC",sans-serif';
const c=document.getElementById('c');c.width=W*K;c.height=H*K;const g=c.getContext('2d');
const IM={},FR={},FPS=15;for(const k in IMS){if(typeof IMS[k]==='string'){IM[k]=new Image();IM[k].src=IMS[k];}else IM[k]=IMS[k];}
function clipPath(s,t){const m=IM[s.im];let i=Math.max(0,Math.floor((t-s.a+m.off)*FPS));const P=2*(m.n-1);i=i%P;if(i>=m.n)i=P-i;return m.dir+'/'+String(i+1).padStart(4,'0')+'.jpg';}
function prep(t){const need=new Set(),ps=[];SEG.forEach(s=>{if(IM[s.im].clip&&t>=s.a-0.6&&t<=s.b+0.6){const p=clipPath(s,t);need.add(p);if(!FR[p]){FR[p]=new Image();FR[p].src=p;}ps.push(FR[p].decode().catch(()=>0));}});for(const p in FR)if(!need.has(p))delete FR[p];return Promise.all(ps);}
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),ease=x=>{x=clamp(x);return 0.5-0.5*Math.cos(Math.PI*x)};
const SEG=[];TL.forEach(([a,b,s,im],i)=>{if(!SEG.length||SEG[SEG.length-1].im!==im)SEG.push({im,a:i?a-0.25:0});});
const LAST=TL[TL.length-1][1];SEG.forEach((s,i)=>s.b=i<SEG.length-1?SEG[i+1].a:LAST+1.2);
const DUST=[...Array(70)].map((_,i)=>({x:(i*97)%540,y:(i*389)%960,r:0.6+(i%5)*0.35,s:6+(i%7)*3,ph:i}));
function drawImg(s,i,t,al){if(al<=0)return;const im=IM[s.im].clip?FR[clipPath(s,t)]:IM[s.im];if(!im||!im.complete||!im.width)return;const p=clamp((t-s.a)/(s.b-s.a+0.6));const z=i%2==0?1.0+0.10*p:1.10-0.10*p;
 const px=(i%3-1)*14*(p-0.5);const sc=Math.max(W/im.width,H/im.height)*z;const w=im.width*sc,h=im.height*sc;
 g.save();g.globalAlpha=al;g.drawImage(im,(W-w)/2+px,(H-h)/2-20,w,h);
 if((EP.pulse||[]).includes(s.im)){g.globalCompositeOperation='lighter';g.globalAlpha=al*0.22*(0.5+0.5*Math.sin(t*2*Math.PI/1.1));g.drawImage(im,(W-w)/2+px,(H-h)/2-20,w,h);}g.restore();}
function draw(t){g.setTransform(K,0,0,K,0,0);g.fillStyle='#000';g.fillRect(0,0,W,H);
 SEG.forEach((s,i)=>{const al=Math.min(ease((t-s.a+0.25)/0.5),ease((s.b+0.25-t)/0.5));drawImg(s,i,t,i==0?Math.min(1,ease((s.b+0.25-t)/0.5)):al);});
 const KP=EP.style==='kepu';
 if(!KP)for(const d of DUST){const y=(d.y-t*d.s)%960;g.beginPath();g.arc(d.x+8*Math.sin(t*0.5+d.ph),y<0?y+960:y,d.r,0,7);g.fillStyle=`rgba(140,220,235,${0.25+0.2*Math.sin(t+d.ph)})`;g.fill();}
 let gr=g.createLinearGradient(0,0,0,H);gr.addColorStop(0,'rgba(0,0,0,0.55)');gr.addColorStop(0.14,'rgba(0,0,0,0)');gr.addColorStop(KP?0.72:0.62,'rgba(0,0,0,0)');gr.addColorStop(0.86,KP?'rgba(0,0,0,0.35)':'rgba(0,0,0,0.75)');gr.addColorStop(1,KP?'rgba(0,0,0,0.5)':'rgba(0,0,0,0.85)');g.fillStyle=gr;g.fillRect(0,0,W,H);
 const rg=g.createRadialGradient(W/2,H/2,H*0.3,W/2,H/2,H*0.75);rg.addColorStop(0,'rgba(0,0,0,0)');rg.addColorStop(1,KP?'rgba(0,0,0,0.25)':'rgba(0,0,0,0.5)');g.fillStyle=rg;g.fillRect(0,0,W,H);
 g.textAlign='center';g.textBaseline='middle';g.font=`500 13px ${F}`;g.fillStyle='rgba(255,255,255,0.72)';g.fillText('本视频仅作科学知识普及',250,30);g.fillText('不作为任何医学诊断、治疗或用药依据',250,49);
 const H0=EP.cover?1.4:0.2;const ta=Math.min(ease((t-H0)/0.5),ease((6.0+H0-t)/0.5));if(ta>0){g.save();g.globalAlpha=ta;g.shadowColor='rgba(0,0,0,0.8)';g.shadowBlur=16;g.font=`900 40px ${F}`;g.lineJoin='round';g.lineWidth=8;g.strokeStyle='rgba(0,0,0,0.92)';g.strokeText(EP.hook[0],250,150);g.fillStyle='#fff';g.fillText(EP.hook[0],250,150);g.strokeText(EP.hook[1],250,202);g.fillStyle='#FFE14D';g.fillText(EP.hook[1],250,202);
  if(t>H0+2.8&&EP.tease){g.globalAlpha=ta*ease((t-H0-2.8)/0.5);g.font=`700 22px ${F}`;g.fillStyle=(EP.theme||{}).tease||'#FFD27A';g.fillText(EP.tease,250,252);}g.restore();}
 for(const [a,b,s] of TL){const al=Math.min(ease((t-a+0.05)/0.15),ease((b+0.2-t)/0.15));if(al<=0)continue;const ls=s.split('\n');
  const fs=KP?29:24,lh=KP?42:34,y0=KP?640:730;
  ls.forEach((ln,i)=>{const y=y0-(ls.length-1)*lh/2+i*lh;g.save();g.globalAlpha=al;g.font=`${KP?900:700} ${fs}px ${F}`;g.shadowColor='rgba(0,0,0,0.9)';g.shadowBlur=8;g.lineWidth=KP?6:4;g.strokeStyle=KP?'rgba(0,0,0,0.85)':'rgba(0,0,0,0.6)';g.lineJoin='round';
   const parts=ln.split(/[【】]/);const tw=g.measureText(parts.join('')).width;let x=250-tw/2;g.textAlign='left';
   parts.forEach((p,j)=>{if(!p)return;g.strokeText(p,x,y);g.fillStyle=j%2?((EP.theme||{}).kw||'#FFE14D'):'#fff';g.fillText(p,x,y);x+=g.measureText(p).width;});g.restore();});}
 const ea=ease((t-LAST-0.6)/1.0);if(ea>0){g.fillStyle=`rgba(0,0,0,${ea*0.85})`;g.fillRect(0,0,W,H);g.save();g.globalAlpha=ease((t-LAST-1.0)/0.8);g.font=`800 44px ${F}`;g.fillStyle='#fff';g.fillText(EP.end_title,250,430);g.font=`500 18px ${F}`;g.fillStyle='rgba(255,255,255,0.7)';g.fillText(EP.end_sub,250,490);g.restore();}
 if(EP.cover){const ca=1-ease((t-1.0)/0.4);if(ca>0){const im=IM[EP.cover.img];g.save();g.globalAlpha=ca;g.fillStyle='#000';g.fillRect(0,0,W,H);
  if(im&&im.width){const z=1.0+0.03*clamp(t/1.4);const sc=Math.max(W/im.width,H/im.height)*z;const w=im.width*sc,h=im.height*sc;g.drawImage(im,(W-w)/2,(H-h)/2,w,h);}
  const cg=g.createLinearGradient(0,0,0,H);cg.addColorStop(0,'rgba(0,0,0,0.45)');cg.addColorStop(0.3,'rgba(0,0,0,0.05)');cg.addColorStop(0.42,'rgba(0,0,0,0.4)');cg.addColorStop(0.62,'rgba(0,0,0,0.4)');cg.addColorStop(0.75,'rgba(0,0,0,0.1)');cg.addColorStop(1,'rgba(0,0,0,0.55)');g.fillStyle=cg;g.fillRect(0,0,W,H);
  g.textAlign='center';g.textBaseline='middle';g.lineJoin='round';const cy=EP.cover.y||450;
  let fs=68;g.font=`900 ${fs}px ${F}`;const tw=g.measureText(EP.cover.title).width;if(tw>460){fs=Math.floor(fs*460/tw);g.font=`900 ${fs}px ${F}`;}
  g.shadowColor='rgba(0,0,0,0.85)';g.shadowBlur=18;g.shadowOffsetY=4;g.lineWidth=11;g.strokeStyle='#000';g.strokeText(EP.cover.title,W/2,cy);g.shadowBlur=0;g.shadowOffsetY=0;
  const yg=g.createLinearGradient(0,cy-fs/2,0,cy+fs/2);const TC=(EP.theme||{}).title||['#FFF27A','#FFD21F','#FFA800'];yg.addColorStop(0,TC[0]);yg.addColorStop(0.55,TC[1]);yg.addColorStop(1,TC[2]);g.fillStyle=yg;g.fillText(EP.cover.title,W/2,cy);
  if(EP.cover.sub){let sf=32;g.font=`900 ${sf}px ${F}`;const sw=g.measureText(EP.cover.sub).width;if(sw>470){sf=Math.floor(sf*470/sw);g.font=`900 ${sf}px ${F}`;}const sy=cy+fs*0.5+sf*1.0;
   g.lineWidth=7;g.strokeStyle='rgba(0,0,0,0.9)';g.strokeText(EP.cover.sub,W/2,sy);g.fillStyle='#fff';g.fillText(EP.cover.sub,W/2,sy);}
  g.font=`500 13px ${F}`;g.fillStyle='rgba(255,255,255,0.72)';g.fillText('本视频仅作科学知识普及',W/2,30);g.fillText('不作为任何医学诊断、治疗或用药依据',W/2,49);g.restore();}}
}</script></body></html>"""
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
def clean(s): return s.replace('\n','').replace('「','').replace('」','').replace('【','').replace('】','')
def tts(ep,d):
    import edge_tts
    os.makedirs(f"{d}/audio",exist_ok=True);L=ep["lines"]
    async def go(): await asyncio.gather(*[edge_tts.Communicate(clean(l[0]),ep.get("voice","zh-CN-YunjianNeural"),rate=ep.get("rate","+8%")).save(f"{d}/audio/l{i:02d}.mp3") for i,l in enumerate(L)])
    asyncio.run(go())
    t=1.3 if ep.get("cover") else 0.6;tl=[]
    for i,l in enumerate(L):
        x=dur(f"{d}/audio/l{i:02d}.mp3");tl.append([round(t,2),round(t+x,2),l[0],l[1]]);t+=x+(0.5 if len(l)>2 and l[2] else 0.15)
    json.dump(tl,open(f"{d}/timeline.json","w"),ensure_ascii=False);print("duration",round(t+3.2,1))
def frames(ep,d,K=1,only=None):
    from playwright.sync_api import sync_playwright
    tl=json.load(open(f"{d}/timeline.json"));ims={}
    for k in {l[1] for l in ep["lines"]}|({ep["cover"]["img"]} if ep.get("cover") else set()):
        if k.startswith("clip:"):
            nm,_,off=k[5:].partition("@");cd=f"{d}/clipframes/{nm}_{K}"
            if not os.path.isdir(cd):
                os.makedirs(cd);subprocess.run(["ffmpeg","-v","error","-i",next((x for x in (f"{d}/clips/{nm}.mp4",f"{LIB}/clips/{nm}.mp4") if os.path.exists(x)),f"{d}/clips/{nm}.mp4"),"-vf",f"fps={FPS},scale={540*K}:{960*K}:force_original_aspect_ratio=increase,crop={540*K}:{960*K}","-q:v","3",f"{cd}/%04d.jpg"],check=True)
            ims[k]={"clip":nm,"off":float(off or 0),"n":len(glob.glob(f"{cd}/*.jpg")),"dir":f"clipframes/{nm}_{K}"};continue
        im=Image.open(next(x for b in (f"{d}/img",f"{LIB}/img") for x in (f"{b}/{k}.{e}" for e in ("png","jpg","webp")) if os.path.exists(x))).convert('RGB').resize((640*K,960*K),Image.LANCZOS);b=io.BytesIO();im.save(b,'JPEG',quality=90)
        ims[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    html=HTML.replace('__EP__',json.dumps({k:ep.get(k) for k in ["hook","tease","end_title","end_sub","pulse","style","cover","theme"]},ensure_ascii=False)).replace('__TL__',json.dumps(tl,ensure_ascii=False)).replace('__IMS__',json.dumps(ims)).replace('__K__',str(K))
    T=tl[-1][1]+3.2;os.makedirs(f"{d}/frames",exist_ok=True)
    for f in glob.glob(f"{d}/frames/*"): os.remove(f)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path=CHROME,args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={"width":540*K,"height":960*K});open(f"{d}/_render.html","w").write(html);pg.goto("file://"+os.path.abspath(f"{d}/_render.html"))
        pg.evaluate("Promise.all([document.fonts.load('800 20px \"Noto Sans CJK SC\"'),document.fonts.load('500 20px \"Noto Sans CJK SC\"'),...Object.values(IM).filter(i=>i.decode).map(i=>i.decode())])")
        ts=only if only is not None else [i/FPS for i in range(int(T*FPS))]
        for i,t in enumerate(ts):
            u=pg.evaluate("async t=>{await prep(t);draw(t);return c.toDataURL('image/jpeg',0.92)}",t)
            open(f"{d}/pv_{i:02d}.jpg" if only is not None else f"{d}/frames/f{i:04d}.jpg","wb").write(base64.b64decode(u.split(',')[1]))
        b.close()
    return tl,T
def preview(ep,d):
    tl=json.load(open(f"{d}/timeline.json"));idx=sorted({0,1,len(tl)//4,len(tl)//2,3*len(tl)//4,len(tl)-4,len(tl)-1})
    ts=[3.6]+[tl[i][0]+0.6 for i in idx]+[tl[-1][1]+2.8];frames(ep,d,1,ts)
    W,H=216,384;sheet=Image.new('RGB',(W*5,H*2))
    for i in range(len(ts)): sheet.paste(Image.open(f"{d}/pv_{i:02d}.jpg").resize((W,H)),((i%5)*W,(i//5)*H))
    sheet.save(f"{d}/contact.png");print("contact",f"{d}/contact.png")
def render(ep,d,hd=False):
    K=2 if hd else 1;tl,T=frames(ep,d,K);name=ep["name"]+("_HD_1080x1920" if hd else "_小样_540x960")
    ins=[];fl=[]
    for i,(a,b,s,_) in enumerate(tl): ins+=["-i",f"{d}/audio/l{i:02d}.mp3"];ms=int(a*1000);fl.append(f"[{i}:a]adelay={ms}|{ms}[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(tl)))+f"amix=inputs={len(tl)}:normalize=0,apad[out]")
    subprocess.run(["ffmpeg","-y","-loglevel","error",*ins,"-filter_complex",";".join(fl),"-map","[out]","-t",str(T),"-ar","44100",f"{d}/vo.wav"],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",f"{d}/frames/f%04d.jpg","-i",f"{d}/vo.wav","-c:v","libx264","-pix_fmt","yuv420p","-crf","20","-c:a","aac","-b:a","128k","-shortest","-movflags","+faststart",f"{d}/{name}.mp4"],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{d}/vo.wav","-b:a","160k",f"{d}/{ep['name']}_配音.mp3"],check=True)
    def ts(s): ms=int(round(s*1000));return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
    open(f"{d}/{ep['name']}.srt","w",encoding="utf-8").write("\n".join(f"{i+1}\n{ts(a)} --> {ts(b+0.15)}\n{s.replace('【','').replace('】','')}\n" for i,(a,b,s,_) in enumerate(tl)))
    if ep.get("cover"): subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","0.3","-i",f"{d}/{name}.mp4","-frames:v","1","-q:v","2",f"{d}/{ep['name']}_封面.jpg"],check=True)
    print("done",f"{d}/{name}.mp4",round(T,1))
def bgm(ep,d,music,hd=True):
    v=f"{d}/{ep['name']}"+("_HD_1080x1920" if hd else "_小样_540x960")+".mp4";D=dur(v);o=v[:-4]+"_配乐.mp4"
    F="aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo"
    fc=(f"[1:a]loudnorm=I=-27,{F},atrim=0:{D},afade=t=in:d=1.5,afade=t=out:st={D-4}:d=4[m];[0:a]{F},asplit[v][sc];"
        "[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=60:release=700[md];"
        "[v][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5,aresample=44100[a]")
    subprocess.run(["ffmpeg","-v","error","-y","-i",v,"-stream_loop","-1","-i",music,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-t",str(D),"-movflags","+faststart",o],check=True)
    print("done",o)
if __name__=="__main__":
    f=sys.argv[1];d=os.path.dirname(os.path.abspath(f));ep=json.load(open(f));cmd=sys.argv[2];hd="--hd" in sys.argv
    if cmd in("tts","all"): tts(ep,d)
    if cmd in("preview","all"): preview(ep,d)
    if cmd in("render","all"): render(ep,d,hd)
    if cmd=="bgm": bgm(ep,d,sys.argv[3],hd)
    if cmd=="final":
        render(ep,d,True);bgm(ep,d,sys.argv[3] if len(sys.argv)>3 and not sys.argv[3].startswith("--") else os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","music","river_flows_in_you.mp3"),True)
        v=f"{d}/{ep['name']}_HD_1080x1920";os.replace(v+"_配乐.mp4",v+".mp4");print("final",v+".mp4")

