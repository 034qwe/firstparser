import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 
from create_bot  import dp,bot 
from aiogram import types,Dispatcher
from keyboards.lang_kb import language

async def wiki_main_text(message:types.Message):

    text = message.text.replace("/search",'').replace('\n','').replace(' ','_')
    print(language)

    headers = {
                'User-Agent': UserAgent().random
            }

    url = f"https://{language}.wikipedia.org/wiki/{text}"
    r = requests.get(url=url,headers=headers)

    soup = BeautifulSoup(r.text,'lxml')
    try:
        request= soup.find('div',class_='mw-parser-output').find_all('p')
        
        text=''
        for i,j in enumerate(request):     
            if i <=2:
                text+=j.text
            else:
                await message.answer(text)
                break
    except:
        await message.answer('nothing was found')
    
       
def register_handlers_maintext(dp:Dispatcher):
    dp.register_message_handler(wiki_main_text,commands=['search'])
