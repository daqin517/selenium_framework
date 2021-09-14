from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import *
import os,time
import requests
from PIL import Image
from io import BytesIO
from skimage import io

img_list = []
img_no = 1
url = Config().get('new_pifu')
data_path = os.path.join(DATA_PATH,'new_pifu')
print(data_path)
locator_hero = (By.XPATH,'//*[@class="p_newhero"]/div/div/ul/li[7]/a')


dr = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
dr.get(url)
# dr.maximize_window()
time.sleep(2)

hero_list = dr.find_elements(*locator_hero)
# print(hero_list)
for hero in hero_list:
    img_list.append(hero.get_attribute('href'))

# print(img_list)

#url读取图片方法一：PIL+requests
# for img_url in img_list:
#     re = requests.get(img_url)
#     img = Image.open(BytesIO(re.content))
#     img.save(os.path.join(data_path, f'{img_no}.png'))
#     img_no += 1

#url读取图片方法二：skimage
for img_url in img_list:




time.sleep(5)
dr.quit()