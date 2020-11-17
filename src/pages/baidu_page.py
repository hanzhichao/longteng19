from logz import log, logit

from src.pages.base_page import BasePage


class BaiduPage(BasePage):
    search_ipt_loc = ('id', 'kw')
    search_btn_loc = ('id', 'su')

    def launch(self):
        self.driver.get('https://www.baidu.com/')

    def input_keyword(self, keyword):
        log.info(f'输入关键字: {keyword}')
        elm = self.driver.find_element(*self.search_ipt_loc)
        elm.clear()
        elm.send_keys(keyword)

    def click_search_btn(self):
        log.info(f'点击搜索按钮')
        self.driver.find_element(*self.search_btn_loc).click()

    def search(self, keyword):
        self.input_keyword(keyword)
        self.click_search_btn()