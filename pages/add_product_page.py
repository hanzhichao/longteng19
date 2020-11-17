from pages.base_page import Page
from utils.log import log


class AddProductPage(Page):
    product_name = ('name', 'goods_name')  # 商品名称输入框
    cate_name = ('id', 'cat_name')  # 商品分类输入框
    shop_price = ('name', 'shop_price')  # 本店售价输入框
    sure = ('id', 'goods_info_submit')  # 确定按钮

    def input_product_name(self, name):
        log.info(f'输入商品名称：{name}')
        self.input_to(self.product_name, name)

    def input_cate_name(self, cate):
        log.info(f'输入商品分类：{cate}')
        self.input_to(self.cate_name, cate)

    def input_shop_price(self, price):
        log.info(f'输入本店售价：{price}')
        self.input_to(self.shop_price, price)

    def click_sure(self):
        log.info('点击确定按钮')
        self.click(self.sure)


if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    from pages.menu_page import MenuPage

    driver = webdriver.Chrome()
    p1 = LoginPage(driver)
    p1.login('admin', '123456')
    p1.wait(2)
    p2 = MenuPage(driver)
    p2.click_menus('商品管理', '添加新商品')
    p2.wait(5)

    p3 = AddProductPage(driver)
    p3.switch_in('main-frame')
    p3.input_product_name('dell电脑')
    p3.input_cate_name('电脑')
    p3.input_shop_price('3999')
    p3.click_sure()
    p3.switch_out()
