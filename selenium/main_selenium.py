from selenium import webdriver
import time 

driver = webdriver.Chrome("D:/programer/projects/firstparser-main/firstparser-main/firstparser\selenium/chromedriver.exe")
url = 'https://www.deepl.com/ru/translator#ru/en/привет'

try:
    driver.get(url=url)
    time.sleep(3)
except:
    print('bad')
