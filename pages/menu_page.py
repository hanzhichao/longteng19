from pages.base_page import Page
from utils.log import log


class MenuPage(Page):
    def click_menu(self, menu):
        log.info(f'点击菜单: {menu}')
        self.driver.find_element('link text', menu).click()

    def click_menus(self, menu, sub_menu):
        self.switch_in('menu-frame')
        self.click_menu(menu)
        self.wait(0.2)
        self.click_menu(sub_menu)
        self.switch_out()


if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage

    driver = webdriver.Chrome()
    p1 = LoginPage(driver)
    p1.login('admin', '123456')
    p1.wait(2)
    p2 = MenuPage(driver)
    p2.click_menus('商品管理', '添加新商品')