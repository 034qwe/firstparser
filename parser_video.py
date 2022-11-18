import requests 
import fake_useragent


ua =fake_useragent.UserAgent()
h = {
    'User-Agent':ua.random
}
url = 'https://v16-webapp.tiktok.com/14410f70a3522c7f67d22e94bf099721/6373e0d7/video/tos/useast2a/tos-useast2a-ve-0068c004/0ec5f75ea9d44ac58f7bd0e7d3d5ba9a/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=6120&bt=3060&cs=0&ds=3&ft=IecA0o6VD12Nv10XuZIxRnbjYlJG-UjNSiAVi9&mime_type=video_mp4&qs=0&rc=aGQ3OTo7PDRmOzg7OzxpPEBpajZqNWc6ZmR0ZTMzNzczM0A2XmAyM2BgXzYxNGMwYF8vYSNsXmovcjRfMHNgLS1kMTZzcw%3D%3D&l=2022111512561101019205217420078658&btag=80000https://v16-webapp.tiktok.com/14410f70a3522c7f67d22e94bf099721/6373e0d7/video/tos/useast2a/tos-useast2a-ve-0068c004/0ec5f75ea9d44ac58f7bd0e7d3d5ba9a/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=6120&bt=3060&cs=0&ds=3&ft=IecA0o6VD12Nv10XuZIxRnbjYlJG-UjNSiAVi9&mime_type=video_mp4&qs=0&rc=aGQ3OTo7PDRmOzg7OzxpPEBpajZqNWc6ZmR0ZTMzNzczM0A2XmAyM2BgXzYxNGMwYF8vYSNsXmovcjRfMHNgLS1kMTZzcw%3D%3D&l=2022111512561101019205217420078658&btag=80000'
r = requests.get(url,headers=h, stream=True)

with open('1.mp4', 'wb') as fw:
    for i in r.iter_content(chunk_size=1024 * 100):
        fw.write(i)
