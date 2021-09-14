import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser():
    def __init__(self,browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]   #调用webdriver.Chrome()
        else:
            raise UnSupportBrowserTypeError('仅支持%s类型的浏览器！'% (',').join(TYPES.keys()))
        self.driver = None

    def get(self,url,maximize_window=True):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        return self


    def save_screen_shot(self,name='screen_shot'): #name为截图保存的名字
        date = time.strftime('%Y%m%d',time.localtime())
        screen_shot_path = REPORT_PATH + '\screenshot_%s' % date
        if not os.path.exists(screen_shot_path):
            os.makedirs(screen_shot_path)

        tm = time.strftime('%H%M%S',time.localtime())
        screenshot = self.driver.save_screenshot(screen_shot_path + r'\\%s_%s.png'%(name,tm))

    def quit(self):
        self.driver.quit()


# if __name__ == '__main__':
#      browser = Browser(browser_type='chrome')
#      browser.get('https://www.baidu.com',maximize_window=False)
#      screen = browser.save_screen_shot('test')
#      browser.quit()




