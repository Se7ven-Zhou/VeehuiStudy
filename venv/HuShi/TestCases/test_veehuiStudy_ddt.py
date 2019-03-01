# coding:utf-8

import requests,urllib3,unittest
import os,time,ddt
import HuShi.Config.SignatureConfig,HuShi.Config.TestDataConfig
from HuShi.Common.ReadData import ReadData
from HuShi.Common.ReadDataDDT import ReadDataDDT
from HuShi.Common.MyLogger import MyLogger
from HuShi.Common.PackageInfo import PackageInfo
from HuShi.Config.EnvironmentConfig import Environment
from HuShi.Common.WriteExcel import WriteExcel
from HuShi.Common.WriteReport import WriteReport
from HuShi.Common.KeyIssue import KeyIssue
from HuShi.Common.ConnectSQL import ConnectSQL
from HuShi.Common.SendMail import SendMail
from HuShi.Common.GetLatestReport import GetLatestReport
from HuShi.Common.Verify import Verify


data_ddt = ReadDataDDT(HuShi.Config.TestDataConfig.Excel_name).getData()

@ddt.ddt
class test_Requests(unittest.TestCase):

    def __init__(self,method):
        super(test_Requests, self).__init__(method)
        self.headers = HuShi.Config.SignatureConfig.headers

    @ddt.data(*data_ddt)
    def test_requests(self,data):

        WriteExcel().creatExcel()
        url = Environment().Test() + data["api"]
        time.sleep(0.5)
        # 请求
        result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)
        MyLogger().info("<请求:\t" + url +">\t<参数:" + data["params"] +">\t<结果:"+ result.text)
        # 当前时间
        now = time.strftime('%Y-%m-%d %H:%M')
        # 获取报告行数
        ReportRow = WriteExcel().getMaxRow()


        if int(data["checkType"]) == int(1):
            Verify(data,result,ReportRow).verifyValue()

        elif int(data["checkType"]) == int(2):
            Verify(data,result,ReportRow).verifydata()

        elif int(data["checkType"]) == int(3):
            Verify(data,result,ReportRow).verifydataExist()

        else:
            Verify(data,result,ReportRow).verifyCode()



        #
        # # 判断是否需要SQL校验
        # if int(data["checkType"]) == int(1):
        #     # 链接数据库，查询比对数据
        #     SQL_check_data = Conn_MySQL().Connect(data["SQL_check"])
        #     try:
        #         assert str(data["check_data"]) == str(SQL_check_data["result"])
        #     except:
        #         WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], str(SQL_check_data), result.text)
        #         # Jira提交BUG
        #         # KeyIssue().Commit(data["api"],data["params"],result.text,str(check_data),1,sql=data["check"])
        #         error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + result.text + ">"
        #         Logging().Error(error_info)
        #         raise
        #
        # elif int(data["checkType"]) == int(2):
        #     # 链接数据库，查询比对数据
        #     SQL_check_data = Conn_MySQL().Connect(data["SQL_check"])
        #     try:
        #         assert str(SQL_check_data["result"]) == str(result.json()["result"][data["check_data"]])
        #     except:
        #         WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], str(SQL_check_data),
        #                                    result.text)
        #         # Jira提交BUG
        #         # KeyIssue().Commit(data["api"],data["params"],result.text,str(check_data),1,sql=data["check"])
        #         error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + result.text + ">"
        #         Logging().Error(error_info)
        #         raise
        #
        # elif int(data["checkType"]) == int(3):
        #     # 链接数据库，查询比对数据
        #     SQL_check_data = Conn_MySQL().Connect(data["SQL_check"])
        #     try:
        #         # 传值当前时间，用于比对
        #         data["check_data"] = now
        #         assert str(data["check_data"]) == str(SQL_check_data["result"])
        #     except:
        #         WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], str(SQL_check_data), result.text)
        #         # Jira提交BUG
        #         # KeyIssue().Commit(data["api"],data["params"],result.text,str(check_data),1,sql=data["check"])
        #         error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + result.text + ">"
        #         Logging().Error(error_info)
        #         raise
        #
        # else:
        #     try:
        #         assert result.json()["code"] == str(data["code"])
        #     except:
        #         # 断言错误报告
        #         WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], data["code"], result.text)
        #         # Jira提交BUG
        #         # KeyIssue().Commit(data["api"], data["params"], result.text, data["code"], 0)
        #         error_info = "【断言错误】\t<正确状态码："+ str(data["code"]) +"\t<Response:\t" + result.text + ">"
        #         Logging().Error(error_info)
        #         raise

if __name__ == "__main__":

    unittest.main()
    # Send_Mail().Send()
    # 正则匹配 .*"id":(/d*).*