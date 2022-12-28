from selenium import webdriver
import time 
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from aiogram import types,Dispatcher


headers = {
                'User-Agent': UserAgent().random
            }

async def r_text(message:types.Message):
    text = message.text.replace('/rework','')
    url = f'https://www.deepl.com/ru/translator#uk/en/{text}'

    try:
        driver = webdriver.Chrome(executable_path="D:/programer/projects/firstparser-main/firstparser-main/firstparser\selenium/chromedriver.exe")

        driver.get(url=url)
        time.sleep(1)


        soup = BeautifulSoup(driver.page_source,'lxml')
        a = soup.find('div',class_='lmt__textarea lmt__textarea_dummydiv',id='target-dummydiv')
        await message.answer(a.text)

    except:
        print('bad')

    finally:
        driver.close()
        driver.quit()


def register_handlers_selenium(dp:Dispatcher):
    dp.register_message_handler(r_text,commands=['rework'])

