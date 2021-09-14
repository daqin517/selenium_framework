from test_1.common.browser import Browser

class Page(Browser):
    def __init__(self,page=None,browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            # super(Page,self).__init__(browser_type=browser_type)  #python2.7语法，super()需要加上子类名和对象self
            super().__init__(browser_type=browser_type)  #python3语法

    def get_driver(self):
        return self.driver

    def find_element(self,*args):
        return self.driver.find_element(*args)

    def find_elements(self,*args):
        return self.driver.find_elements(*args)