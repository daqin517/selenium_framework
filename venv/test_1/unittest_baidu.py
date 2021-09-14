import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import *
from utils.log import logger
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email

class TestBaidu(unittest.TestCase):
    url = Config().get('url')
    print(url)
    base_path = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(os.path.dirname(base_path), 'drivers', 'chromedriver.exe')
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_link = (By.XPATH, '//*[@id="content_left"]/div/h3/a')

    def setUp(self):
        # self.dr = webdriver.Chrome(executable_path=self.driver_path)
        self.dr = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.dr.get(self.url)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

    def test_search_for_subtest(self):
        list = ['selenium', '蔡徐坤', '张艺兴']
        for d in list:
            with self.subTest(d=d):
                self.dr.find_element(*self.locator_kw).clear()
                self.dr.find_element(*self.locator_kw).send_keys(d)
            self.dr.find_element(*self.locator_su).click()
            # print(self.dr.current_url)
            time.sleep(5)
            data_list = self.dr.find_elements(*self.locator_link)
            print(type(data_list), '长度为：', len(data_list))
            num = 1
            for data in data_list:
                print(type(data))
                print('第', num, '条：', data.text)
                logger.info(data.text)
                num += 1


    def test_search_1(self):
        self.dr.find_element(*self.locator_kw).send_keys('selenium')
        self.dr.find_element(*self.locator_su).click()
        # print(self.dr.current_url)
        time.sleep(5)
        data_list = self.dr.find_elements(*self.locator_link)
        print(type(data_list), '长度为：', len(data_list))
        num = 1
        for data in data_list:
            print(type(data))
            print('第', num, '条：', data.text)
            logger.info(data.text)
            num += 1

    def test_search_2(self):
        self.dr.find_element(*self.locator_kw).send_keys('蔡徐坤')
        self.dr.find_element(*self.locator_su).click()
        # print(self.dr.current_url)
        time.sleep(5)
        data_list = self.dr.find_elements(*self.locator_link)
        print(type(data_list), '长度为：', len(data_list))
        num = 1
        for data in data_list:
            print(type(data))
            print('第', num, '条：', data.text)
            logger.info(data.text)
            num += 1

    def test_search_3(self):
        self.dr.find_element(*self.locator_kw).send_keys('张艺兴')
        self.dr.find_element(*self.locator_su).click()
        # print(self.dr.current_url)
        time.sleep(5)
        data_list = self.dr.find_elements(*self.locator_link)
        print(type(data_list), '长度为：', len(data_list))
        num = 1
        for data in data_list:
            print(type(data))
            print('第', num, '条：', data.text)
            logger.info(data.text)
            num += 1



if __name__ == '__main__':
    # unittest.main()
    report = os.path.join(REPORT_PATH, 'testreport.html')
    st = unittest.TestSuite()
    st.addTests([TestBaidu('test_search_for_subtest'),TestBaidu('test_search_1'),TestBaidu('test_search_2'),TestBaidu('test_search_3')])
    # print(st)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='baidu测试报告', description='执行人：大钦')
        runner.run(st)
    e = Email('smtp.qq.com', '921497786@qq.com', 'dkomoybhicppbbdd', '921497786@qq.com', 'Test_Mail',
              massage='测试（this is a massage!）', path=report)
    e.send()
