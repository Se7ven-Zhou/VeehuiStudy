# coding:utf-8

import sys
sys.path.append("C:/Users/Administrator/PycharmProjects/pythonStudy/venv")
import os
import time
import unittest
from HuShi.TestCases import Monitor_VeehuiStudy

if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径

    suite.addTest(loader.loadTestsFromModule(Monitor_VeehuiStudy))

    runner.run(suite)

