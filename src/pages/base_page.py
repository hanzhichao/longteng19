from selenium import webdriver
from time import sleep


class BasePage(object):
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def wait(self, second=1):
        sleep(second)