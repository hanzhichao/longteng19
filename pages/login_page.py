from pages.base_page import Page
from utils.log import log


class LoginPage(Page):
    username = ('name', 'username')  # 用户名输入框
    password = ('name', 'password')  # 密码输入框
    submit = ('class name', 'button2')  # 登录按钮

    def open(self):
        log.info('打开登录页面')
        self.driver.get('http://39.104.14.232/newecshop/admin/privilege.php?act=login')

    def input_username(self, username):
        log.info(f'输入用户名：{username}')
        self.input_to(self.username, username)

    def input_password(self, password):
        log.info(f'输入密码：*****')
        self.input_to(self.password, password)

    def click_login(self):
        log.info(f'点击登录按钮')
        self.click(self.submit)

    def login(self, username, password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        if '您输入的帐号信息不正确。' in self.driver.page_source:
            return False
        return True


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    p = LoginPage(driver)
    p.login('admin', '123456')


