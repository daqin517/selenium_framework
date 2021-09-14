import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils.scroll_move import *
from utils.config import Config,SCREEN_PATH
from utils.log import logger

url = Config().get('url')
print(url)
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
driver_path = os.path.join(base_path,'drivers','chromedriver.exe')

dr = webdriver.Chrome(executable_path=driver_path)
dr.get(url)
# dr.maximize_window()
dr.find_element(By.ID, 'kw').send_keys('迪丽热巴')
dr.find_element(By.ID,'su').click()
time.sleep(5)
tm = time.strftime('%Y%m%d-%H%M%S',time.localtime())
print(tm)
dr.get_screenshot_as_file(SCREEN_PATH + r'\\%s.png' % tm)

scroll = Scroll_move(dr)
scroll.scroll_down()
time.sleep(5)
data_list = dr.find_elements(By.XPATH,'//*[@id="content_left"]/div/h3/a')
print(type(data_list),'长度为：',len(data_list))
num = 1
for data in data_list:
    logger.info(data.text)
    print('第', num, '条：', data.text)
    num += 1

dr.quit()