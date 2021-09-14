import os

from utils.config import Config,DRIVER_PATH,SCREEN_PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = Config().get('url')
DRIVER = os.path.join(DRIVER_PATH,'chromedriver.exe')
dr = webdriver.Chrome(executable_path=DRIVER)
dr.get(url)

locator_kw = (By.ID,'kw')
locator_su = (By.ID,'su')
tm = time.strftime("%Y%m%d-%H%M%S",time.localtime())

dr.find_element(*locator_kw).send_keys('迪丽热巴')
dr.find_element(*locator_su).click()
time.sleep(5)

dr.get_screenshot_as_file(SCREEN_PATH + r'\\%s.png' % tm)

time.sleep(2)
dr.quit()