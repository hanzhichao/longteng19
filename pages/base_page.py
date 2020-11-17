"""页面基础类"""
from time import sleep

from selenium import webdriver

from utils.log import log


# class Browser(object):
#     def __init__(self, driver='chrome', headless=False):
#         if driver == 'chrome':
#             if headless is False:
#                 return webdriver.Chrome()
#             else:
#                 options = webdriver.ChromeOptions()
#                 options.headless = True
#                 return webdriver.Chrome(options=options)
#         else:
#             raise NotImplementedError('暂时只支持Chrome浏览器')
#
#
# class Element(object):
#     def __init__(self, by, expr, name=None):
#         self.by = by
#         self.expr = expr
#         self.name = name
#

class Page(object):
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def click(self, elm):
        log.debug(f'点击 {elm}')
        self.driver.find_element(*elm).click()

    def input_to(self, elm, text):
        log.debug(f'向 {elm} 输入 {text}')
        element = self.driver.find_element(*elm)
        element.clear()
        element.send_keys(text)

    def wait(self, second=1):
        sleep(second)


    def switch_in(self, frame):
        log.info(f'切入框架 {frame}')
        self.driver.switch_to.frame(frame)


    def switch_out(self):
        log.info('切出所有框架')
        self.driver.switch_to.default_content()

