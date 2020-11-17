import unittest

from selenium import webdriver


class BaseCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            cls.driver.quit()


