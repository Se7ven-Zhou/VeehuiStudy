# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
import HuShi.Config.params_config
import pytest
import os
import time


class Requests:

    def __init__(self):

        # self.api = "/meeting/search"
        self.signature = HuShi.Config.params_config.signature
        self.token = HuShi.Config.params_config.token
        self.headers = HuShi.Config.params_config.headers



    def test_Requests(self,filename):

        api_list = Read_Data(filename).Get_API()
        params_list = Read_Data(filename).Get_Params()
        code_list = Read_Data(filename).Get_Code()
        name_list = Read_Data(filename).Get_name()

        for item in range(0,len(api_list)):
            n=2
            try:
                params = Parameter().Package_params(params_list[item], signature=self.signature)
                url = Environment().Test() + api_list[item]
                result = requests.post(url, params, headers=self.headers)
                Logging().Info("Request:" + url + "  Parameters:" + str(params))
                assert int(result.json()["code"]) == code_list[item] , WriteReport().Write_Report(n+1,name_list[item], api_list[item], params_list[item], code_list[item], str(result.json()))
            except Exception as error:
                error_info = "<AssertionError> " + str(result.json()["code"]) + "≠" + str(code_list[item]) + " <Response:" + str(result.json()) + ">"
                Logging().Error(error_info)
                raise error

if __name__ == "__main__":
    # api = "/meeting/search"
    # params_dict = {"searchKey": "笑话", "pageNo": 1, "pageSize": 20}
    Requests().test_Requests("test_data.xlsx")