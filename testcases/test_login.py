
import ddt

from pages.login_page import LoginPage
from testcases.base_case import BaseCase
from utils.data import load_csv


@ddt.ddt
class TestLogin(BaseCase):
    def test_login(self):
        """测试正常登陆"""
        page = LoginPage(self.driver)
        result = page.login('admin', '123456')
        self.assertTrue(result)

    def test_login_pwd_err(self):
        """测试密码错误登陆"""
        page = LoginPage(self.driver)
        result = page.login('admin', '123')
        self.assertFalse(result)

    @ddt.data(load_csv('users.csv'))
    def test_login_multi(self, item):
        """测试正常登陆"""
        username = item.get('username')
        password = item.get('password')
        page = LoginPage(self.driver)
        result = page.login(username, password)
        self.assertTrue(result)


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=2)