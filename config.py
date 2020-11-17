import os
import logging

from emailz import email


# 目录设置
BASEDIR = os.path.dirname(__file__)
REPORT_DIR = os.path.join(BASEDIR, 'reports')
DATA_DIR = os.path.join(BASEDIR, 'data')


# 日志配置
LOG_LEVEL = logging.INFO
LOG_FILE = os.path.join(REPORT_DIR, 'run.log')
LOG_FILE_MODE = 'a'
LOG_FMT = '%(asctime)s %(levelname)s %(message)s'
# LOG_FMT = '%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(funcName)s %(message)s'


# 邮件配置
email.config('test_results@sina.com', '***', host='smtp.sina.com')