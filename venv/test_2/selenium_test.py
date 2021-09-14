from selenium import webdriver
import time,os

base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
driver_path = os.path.join(base_path,'drivers','chromedriver.exe')
base_url = "https://www.baidu.com"

dr = webdriver.Chrome(executable_path=driver_path)
# dr.maximize_window()
dr.get(base_url)

while True:
    time.sleep(10)
    dr.refresh()


dr.quit()