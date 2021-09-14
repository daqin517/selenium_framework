from selenium.webdriver.common.by import By
from test_1.common.page import Page

class BaiduMainPage(Page):
    loc_search_input = (By.ID,'kw')
    loc_search_button = (By.ID,'su')

    def search(self,kw):
        '''搜索功能'''
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()