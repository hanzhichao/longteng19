import sys
import unittest

from HTMLReport import TestRunner


from config import BASEDIR, email

sys.path.append(BASEDIR)
from suites import login_suite, add_products_suite, all_suite

def run_suite(suite):
    # runner = unittest.TextTestRunner(verbosity=2)
    runner = TestRunner(report_file_name="report",
                        output_path="reports",
                        title="商之翼测试报告",)
    email.send(subject='商之翼测试报告',
               receivers=['superhin@126.com'],
               body='hi, 报告请查看附件',
               attachments=['reports/report.html', 'reports/report.log']
               )
    runner.run(suite)


if __name__ == '__main__':
    run_suite(login_suite)