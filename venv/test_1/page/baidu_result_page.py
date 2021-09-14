from selenium.webdriver.common.by import By
from test_1.page.baidu_main_page import BaiduMainPage

class BaiduResultPage(BaiduMainPage):
    loc_result_links = (By.XPATH,'//*[@id="content_left"]/div/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)