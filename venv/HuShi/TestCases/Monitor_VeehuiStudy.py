# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.readData_DDT import Read_Data_ddt
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
from HuShi.Common.keyIssue import KeyIssue
from HuShi.Common.conn_mysql import Conn_MySQL
from HuShi.Common.sendWX import SendWX
import HuShi.Config.params_config,HuShi.Config.testData_config
import unittest
import os
import time
import ddt

data_ddt = Read_Data_ddt(HuShi.Config.testData_config.Excel_name).Get_Data()

@ddt.ddt
class test_Requests(unittest.TestCase):

    def __init__(self,method):
        super(test_Requests, self).__init__(method)
        self.headers = HuShi.Config.params_config.headers

    @ddt.data(*data_ddt)
    def test_requests(self,data):

        url = Environment().Test() + data["api"]
        time.sleep(0.5)
        # 请求
        result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)

        try:
            if result.json()["message"] == "系统异常":
                SendWX().System_error(data["api"])

            elif result.json()["status"] == str(500):
                SendWX().No_service(data["api"])

            else:
                pass
        except:
            pass

if __name__ == "__main__":

    unittest.main()