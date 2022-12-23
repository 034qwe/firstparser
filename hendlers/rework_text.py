import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from aiogram import types,Dispatcher


headers = {
                'User-Agent': UserAgent().random
            }
async def rework_text(message:types.Message):
    text = message.text.replace('/rework','')
    url ="https://translate.google.com/?hl=ru&sl=auto&tl=ru&text=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82&op=translate"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    a = soup.find('div',class_='QcsUad BDJ8fb')
    print(a)
    await message.answer('1234')

    

def register_handlers_rework(dp:Dispatcher):
    dp.register_message_handler(rework_text,commands=['rework'])

