import os,time
from utils.config import *
from selenium import webdriver
import requests
from PIL import Image
from io import BytesIO


url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/155/155.jpg'
data_path = os.path.join(DATA_PATH,'wangzhe')
# dr = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
response = requests.get(url)

img = Image.open(BytesIO(response.content))
img.save(data_path+'\\155.jpg')
img.show()