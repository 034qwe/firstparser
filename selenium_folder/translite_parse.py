from selenium import webdriver
import time 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from aiogram import types,Dispatcher


async def translator(message:types.Message):
    text = message.text.replace('/translation','')

    url = f'https://www.deepl.com/ru/translator#ru/zh/{text}'

    driver = webdriver.Chrome(executable_path="D:/programer/projects/firstparser-main/firstparser-main/firstparser\selenium/chromedriver.exe")

    driver.get(url=url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source,'lxml')
    a = soup.find('div',class_='lmt__textarea lmt__textarea_dummydiv',id='target-dummydiv')

    await message.answer(a.text)