"""日志记录器封装"""
import logging

from config import LOG_LEVEL, LOG_FILE, LOG_FILE_MODE, LOG_FMT


def get_logger(name='WebAuto'):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # 用于输出到终端
    hander1 = logging.StreamHandler()
    hander2 = logging.FileHandler(
        filename=LOG_FILE, mode=LOG_FILE_MODE, encoding='utf-8'
    )

    # 日志格式
    fmt = logging.Formatter(LOG_FMT)
    hander1.setFormatter(fmt)
    hander2.setFormatter(fmt)

    logger.addHandler(hander1)
    logger.addHandler(hander2)
    return logger


log = get_logger()


if __name__ == '__main__':
    log.info('测试信息')