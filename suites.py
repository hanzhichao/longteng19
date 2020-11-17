import unittest

from testcases.test_login import TestLogin
from testcases.test_add_product import TestAddProduct


loader = unittest.TestLoader()

# 所有用例集合
all_suite = unittest.defaultTestLoader.discover('testcases', pattern='test*.py')


# 登录用例集合
login_suite = loader.loadTestsFromTestCase(TestLogin)

# 添加商品
add_products_suite = unittest.TestSuite()
add_products_suite.addTests(
    [TestAddProduct('test_login'),
     TestAddProduct('test_click_menu'),
     TestAddProduct('test_add_product2')
     ]
)


