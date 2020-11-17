import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.add_product_page import AddProductPage
from testcases.base_case import BaseCase


class TestAddProduct(BaseCase):
    @unittest.skip('暂时跳过')
    def test_add_product(self):
        page = LoginPage(self.driver)
        result = page.login('admin', '123456')
        self.assertTrue(result)
        page = MenuPage(self.driver)
        page.click_menus('商品管理', '添加新商品')
        page = AddProductPage(self.driver)
        page.input_product_name('Dell电脑')
        page.input_cate_name('电脑')
        page.input_shop_price('3999')
        page.click_sure()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        """测试登录"""
        page = LoginPage(self.driver)
        result = page.login('admin', '123456')
        self.assertTrue(result)

    def test_click_menu(self):
        page = MenuPage(self.driver)
        page.click_menus('商品管理', '添加新商品')
        # 此处应该有断言

    def test_add_product2(self):
        page = AddProductPage(self.driver)
        page.input_product_name('Dell电脑')
        page.input_cate_name('电脑')
        page.input_shop_price('3999')
        page.click_sure()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([
        TestAddProduct('test_login'),
        TestAddProduct('test_click_menu'),
        TestAddProduct('test_add_product2'),
    ])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

