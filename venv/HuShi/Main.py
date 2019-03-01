# coding:utf-8

import sys
sys.path.append("C:/Users/Administrator/PycharmProjects/pythonStudy/venv")
import os
import time
import unittest
import HuShi.Config.SignatureConfig
import HuShi.Config.TestDataConfig
import HTMLTestRunnerNew
from HuShi.Config.EnvironmentConfig import Environment
from HuShi.Common.InitializeDada import InitializeDada
from HuShi.Common.MyLogger import MyLogger
from HuShi.TestCases import test_veehuiStudy_ddt
from HuShi.Common.SendMail import SendMail
from openpyxl import load_workbook
from openpyxl import Workbook

if __name__ == "__main__":
    # 初始化账号
    # sql = "DELETE FROM user_operation_record WHERE user_id=58 AND operation_type_code=02 order by create_time DESC LIMIT 1"
    # InitializeDada().initData(sql)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径
    # 加载套件
    suite.addTest(loader.loadTestsFromModule(test_veehuiStudy_ddt))
    # 报告信息
    startTime = time.time() # 获取开始运行时间
    report_address = os.getcwd() + "\Reports"
    report_name = "接口自动化测试" + time.strftime("%Y-%m-%d_%H_%M_%S") + ".html"
    report_path = os.path.join(report_address,report_name)
    # 开跑
    with open(report_path, "wb+") as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="VeehuiStudy_API", tester="Seven")
        runner.run(suite)

    finishTime = time.time()    # 获取结束运行时间

    # 发送邮件信息
    testTime = float(finishTime) - float(startTime)
    filePath = os.getcwd()  +"/TestDatas/" + HuShi.Config.TestDataConfig.Excel_name
    file = load_workbook(filePath)
    sheet = file.get_sheet_by_name(HuShi.Config.TestDataConfig.Sheet_name)
    count = sheet.max_row
    SendMail().send(count,testTime)
    file.save(filePath)
