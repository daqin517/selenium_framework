#coding=utf8
from selenium import webdriver
import time
import pprint
import os

base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
driver_path = os.path.join(base_path,'drivers','chromedriver.exe')
base_url = "https://www.baidu.com"
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
driver.get(base_url)
#打印所有cookie
print(driver.get_cookies())
print('-----------------------------')
pprint.pprint(driver.get_cookies())
driver.quit()