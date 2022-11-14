import requests 

h = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
url = 'https://www.youtube.com/watch?v=jmJsoWs4IOE'
r = requests.get(url, stream=True)

with open('1.mp4', 'wb') as fw:
    for i in r.iter_content(chunk_size=1024 * 100):
        fw.write(i)
 