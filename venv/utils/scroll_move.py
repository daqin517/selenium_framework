import time

class Scroll_move():
    def __init__(self,driver):
        self.dr = driver

    def scroll_down(self):
        for i in range(3):
            js = "var q=document.documentElement.scrollTop=" + str(i*1000)
            self.dr.execute_script(js)
            time.sleep(2)

    def scroll_up(self):
        js = "var q=document.documentElement.scrollTop=0;"
        self.dr.execute_script(js)
        time.sleep(2)

    def scroll_left(self):
        js = "var q=document.documentElement.scrollLeft=0;"
        self.dr.execute_script(js)
        time.sleep(2)

    def scroll_right(self):
        for i in range(3):
            js = "var q=document.documentElement.scrollLeft=" + str(i*500)
            self.dr.execute_script(js)
            time.sleep(2)
