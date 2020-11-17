import unittest
from selenium import webdriver
from utils.log import log


class BaseCase(unittest.TestCase):
    def setUp(self):
        log.info('启动Chrome浏览器')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        log.info('退出浏览器')
        self.driver.quit()

