import time
import os
from utils.log import logger
from test_1.page.baidu_result_page import BaiduMainPage,BaiduResultPage
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
from utils.config import Config,REPORT_PATH

class BaiduTest(unittest.TestCase):
    url = Config().get('url')
    # print('-----------1111------------')
    # print('url--------',url)

    def sub_setUp(self):
        self.page = BaiduMainPage().get(self.url,maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        keys = ['zhangyixing','huangbo']
        for d in keys:
            with self.subTest(d=d):
                self.sub_setUp()
                self.page.search(d)
                time.sleep(2)
                self.page = BaiduResultPage(self.page)
                links = self.page.result_links
                print(links)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    # unittest.main()
    report = os.path.join(REPORT_PATH,'test_baidu.html')
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=1,title='百度测试',description='daqin')
        runner.run(BaiduTest('test_search'))