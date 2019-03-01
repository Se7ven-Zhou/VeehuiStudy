# coding:utf-8

import logging
import os
import time

class MyLogger:

    def __init__(self):

        self.address = self.address = os.path.split(os.path.dirname(__file__))[0] + "\Logs"
        self.log_name = time.strftime("%Y-%m-%d")+".txt"
        self.log_path = os.path.join(self.address,self.log_name)

        # 生成日志文件,日期命名，没有就创建
        if os.path.exists(self.log_path):
            file = open(self.log_path, "a")
            file.close()
        else:
            file = open(self.log_path, "w")
            file.close()

        self.logger = logging.getLogger(self.log_path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(module)s]--日志信息：%(message)s")
        # # 设置控制台日志
        # sh = logging.StreamHandler()
        # sh.setFormatter(fmt)
        # sh.setLevel(logging.DEBUG)
        # 设置文件日志
        fh = logging.FileHandler(self.log_path, encoding="utf-8")
        fh.setFormatter(fmt)
        fh.setLevel(logging.DEBUG)

        # self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    logger = MyLogger()
    logger.debug('一个debug信息')
    logger.info('一个info信息')
    logger.warning('一个warning信息')
    try:
        error_message
    except Exception as error:
        logger.error(error)
    logger.critical('一个致命critical信息')