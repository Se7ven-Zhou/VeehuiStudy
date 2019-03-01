# coding:utf-8

import requests
import urllib3
import unittest
import os,time
import HuShi.Config.SignatureConfig,HuShi.Config.TestDataConfig
from HuShi.Common.ReadData import ReadData
from HuShi.Common.ReadDataDDT import ReadDataDDT
from HuShi.Common.MyLogger import MyLogger
from HuShi.Common.PackageInfo import PackageInfo
from HuShi.Config.EnvironmentConfig import Environment
from HuShi.Common.WriteExcel import WriteExcel
from HuShi.Common.KeyIssue import KeyIssue
from HuShi.Common.ConnectSQL import ConnectSQL
from HuShi.Common.SendMail import SendMail
from HuShi.Common.GetLatestReport import GetLatestReport


class Verify:

    def __init__(self, data, result,ReportRow):

        self.data = data
        self.result = result
        self.ReportRow = int(ReportRow)

    # 数值校验
    def verifyValue(self):

        SQL_check_data = ConnectSQL().connectMySQL(self.data["SQL_check"])
        try:
            assert str(self.data["check_data"]) == str(SQL_check_data["result"])
        except:
            WriteExcel().writeErrorInfo(self.ReportRow + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_data), self.result.text)
            # Jira提交BUG
            # KeyIssue().commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + self.result.text + ">"
            MyLogger().error(error_info)
            raise

    # 字段校验
    def verifydata(self)\
            :
        SQL_check_data = ConnectSQL().connectMySQL(self.data["SQL_check"])
        try:
            assert str(SQL_check_data["result"]) == str(
                self.result.json()["result"][self.data["check_data"]])
        except:
            WriteExcel().writeErrorInfo(self.ReportRow + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_data),
                                       self.result.text)
            # Jira提交BUG
            # KeyIssue().commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + self.result.text + ">"
            MyLogger().error(error_info)
            raise

    # 验证数据是否存在
    def verifydataExist(self):

        SQL_check_data = ConnectSQL().connectMySQL(self.data["SQL_check"])
        try:
            # 传值当前时间，用于比对
            # self.data["check_data"] = time.strftime("%Y-%m-%d %H:%M")
            #
            # assert str(self.data["check_data"]) == str(SQL_check_data["result"])
            CurrentTime = time.strftime("%Y-%m-%d %H:%M")

            assert str(CurrentTime) == str(SQL_check_data["result"])
        except:
            WriteExcel().writeErrorInfo(self.ReportRow + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_data), self.result.text)
            # Jira提交BUG
            # KeyIssue().commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + self.result.text + ">"
            MyLogger().error(error_info)
            raise


    def verifyCode(self):
        try:
            assert self.result.json()["code"] == str(self.data["code"])
        except:
            # 断言错误报告
            WriteExcel().writeErrorInfo(self.ReportRow + 1, self.data["name"], self.data["api"], self.data["params"], self.data["code"],
                                       self.result.text)
            # Jira提交BUG
            # KeyIssue().commit(self.data["api"], self.data["params"], self.result.text, self.data["code"], 0)
            error_info = "【断言错误】\t<正确状态码：" + str(self.data["code"]) + "\t<Response:\t" + self.result.text + ">"
            MyLogger().error(error_info)
            raise