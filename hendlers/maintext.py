import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 
from create_bot  import dp,bot 
from aiogram import types,Dispatcher

async def wiki_main_text(message:types.Message):

    text = message.text.replace("/search",'').replace('\n','').replace(' ','_')
    print(text)

    headers = {
                'User-Agent': UserAgent().random
            }

    url = "https://uk.wikipedia.org/wiki/"+text
    r = requests.get(url=url,headers=headers)

    soup = BeautifulSoup(r.text,'lxml')
    request= soup.find('p')
    await message.answer(request.text)

def register_handlers_maintext(dp:Dispatcher):
    dp.register_message_handler(wiki_main_text,commands=['search'])
    