from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
data = ''
city = 'mumbai'
driver = webdriver.Firefox()
driver.get(f'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName={city}')

last = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    try:
        WebDriverWait(driver,30).until(lambda d: d.execute_script('return document.body.scrollHeight') > last)
    except:
        break
    last = driver.execute_script('return document.body.scrollHeight')

with open('magic_bricks_project/data.html','w',encoding = 'utf-8') as file:
    file.write(driver.page_source)







