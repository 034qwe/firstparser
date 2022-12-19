import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from aiogram import types,Dispatcher


headers = {
                'User-Agent': UserAgent().random
            }

async def download_youtube(message:types.Message):
    text = message.text.replace('/video','').replace('\n','').replace(' ','')
    url='https://www.youtube.com/watch?v=KdiM-dS7nAU'

    r = requests.get(url=url,headers=headers)
    print(r)
    soup = BeautifulSoup(r.text,'lxml')
    element = soup.find('div',class_="html5-video-container")
    await message.answer(element)


def register_handlers_youtube(dp:Dispatcher):
    dp.register_message_handler(download_youtube,commands=['video'])