import unittest

from src.testcases.base_case import BaseCase
from src.pages.baidu_page import BaiduPage


class TestBaidu(BaseCase):
    def test_search(self):
        """
        测试百度搜索
        tag:demo
        level:5
        """
        baidu = BaiduPage(self.driver)
        baidu.launch()
        baidu.search('博客园 韩志超')
        self.driver.save_screenshot('baidu.png')
        self.images = ['baidu.png']
        baidu.wait()
        self.assertIn('博客园 韩志超', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
