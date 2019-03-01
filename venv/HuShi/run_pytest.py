# coding:utf-8

import pytest
import os
import time


if __name__ == "__main__":

    report_path = os.getcwd() + "\Reports" # 测试报告地址

    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_name = "Smoke_Test" + now + ".html"

    test_report_path = os.path.join(report_path,report_name)

    pytest.main(["-m","smoke","--html",test_report_path])