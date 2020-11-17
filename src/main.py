import unittest
from logz import log
from htmlrunner import HTMLRunner
from  HTMLReport import TestRunner

log.format = '%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(funcName)s %(message)s'


def main():
    suite = unittest.defaultTestLoader.discover('testcases')
    runner = unittest.TextTestRunner(verbosity=0, buffer=True)
    # runner = HTMLRunner(report_file='report.html', output='', title='Baidu搜索测试')
    runner = TestRunner(report_file_name='report.html', output_path='reports', title='Baidu搜索测试')

    runner.run(suite)


if __name__ == '__main__':
    main()

