import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from aiogram import types,Dispatcher


headers = {
                'User-Agent': UserAgent().random
            }
async def rework_text(message:types.Message):
    text = message.text.replace('/rework','')
    url ="https://www.deepl.com/ru/translator#ru/en/привет"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    a = soup.find('div',class_='lmt__translations_as_text')

    await message.answer(a)
 

def register_handlers_rework(dp:Dispatcher):
    dp.register_message_handler(rework_text,commands=['rework'])

