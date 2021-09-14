# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


mobileEmulation = {'deviceName': 'Apple iPhone 4'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Python3.9.6\chromedriver.exe', chrome_options=options)

driver.get('http://m.baidu.com')

sleep(3)
driver.close()