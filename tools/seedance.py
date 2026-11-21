#!/usr/bin/env python3
"""Seedance image-to-video for organ clips.
Usage: ARK_API_KEY=... python3 seedance.py first_frame.png "prompt" out.mp4 [--dur 6] [--res 720p] [--model doubao-seedance-2-0-260128]"""
import os,sys,json,time,base64,argparse,urllib.request
p=argparse.ArgumentParser();p.add_argument("img");p.add_argument("prompt");p.add_argument("out")
p.add_argument("--dur",type=int,default=6);p.add_argument("--res",default="720p");p.add_argument("--ratio",default="9:16")
p.add_argument("--model",default=os.environ.get("SEEDANCE_MODEL","doubao-seedance-2-0-260128"))
a=p.parse_args();K=os.environ["ARK_API_KEY"];B="https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks"
def req(url,data=None):
    r=urllib.request.Request(url,data=json.dumps(data).encode() if data else None,headers={"Authorization":f"Bearer {K}","Content-Type":"application/json"},method="POST" if data else "GET")
    try: return json.load(urllib.request.urlopen(r,timeout=60))
    except urllib.error.HTTPError as e: sys.exit(f"HTTP {e.code}: {e.read().decode()[:800]}")
mime="image/png" if a.img.lower().endswith(".png") else "image/jpeg"
img="data:%s;base64,%s"%(mime,base64.b64encode(open(a.img,"rb").read()).decode())
t=req(B,{"model":a.model,"content":[{"type":"text","text":a.prompt},{"type":"image_url","image_url":{"url":img},"role":"first_frame"}],
        "resolution":a.res,"ratio":a.ratio,"duration":a.dur,"generate_audio":False,"watermark":False})
tid=t["id"];print("task",tid,flush=True)
while True:
    time.sleep(10);s=req(f"{B}/{tid}");st=s.get("status")
    if st=="succeeded": break
    if st in("failed","cancelled","expired"): sys.exit("FAILED "+json.dumps(s,ensure_ascii=False)[:800])
u=s["content"]["video_url"];urllib.request.urlretrieve(u,a.out);print("done",a.out,s.get("usage"))
