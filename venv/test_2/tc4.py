from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
dr =webdriver.Chrome(options=options)
dr.get('https://www.baidu.com')