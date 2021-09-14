import time,os
from PIL import ImageGrab,Image
from utils.config import SCREEN_PATH


def Screeshot():
    tm = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    print(tm)
    im = ImageGrab.grab()
    im.show()  
    im.save(SCREEN_PATH + r'\\%s.png' % tm)

while True:
    print('截图')
    Screeshot()
    print('暂停')
    time.sleep(10)