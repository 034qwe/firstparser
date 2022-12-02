import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 


headers = {
            'User-Agent': UserAgent().random
        }
request = input()
url = "https://uk.wikipedia.org/wiki/"+request
r = requests.get(url=url,headers=headers)

soup = BeautifulSoup(r.text,'lxml')

a = soup.find('p')
print(a.text)
