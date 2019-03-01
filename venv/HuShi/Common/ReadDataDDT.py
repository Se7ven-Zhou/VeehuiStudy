# coding:utf-8

import os
import HuShi.Config.TestDataConfig
from openpyxl import load_workbook
from openpyxl import Workbook
from HuShi.Common.MyLogger import MyLogger


class ReadDataDDT():

    def __init__(self,filename,address = os.path.split(os.path.dirname(__file__))[0]+"\TestDatas"):

        self.address = address
        self.filename = filename

        self.path = os.path.join(self.address, self.filename)
        try:
            self.file = load_workbook(self.path)
        except Exception as error:
            MyLogger().error(error)
            raise error

        self.sheet = self.file.get_sheet_by_name(HuShi.Config.TestDataConfig.Sheet_name)

    def getData(self):

        params_list = []
        for item in range(2, self.sheet.max_row + 1):
            data_dict = {}
            data_dict["name"] = self.sheet.cell(row=item, column=2).value
            data_dict["api"] = self.sheet.cell(row=item, column=3).value
            data_dict["method"] = self.sheet.cell(row=item, column=4).value
            data_dict["params"] = self.sheet.cell(row=item, column=5).value
            data_dict["code"] = self.sheet.cell(row=item, column=6).value
            data_dict["checkType"] = self.sheet.cell(row=item, column=7).value
            data_dict["check_data"] = self.sheet.cell(row=item, column=8).value
            data_dict["SQL_check"] = self.sheet.cell(row=item, column=9).value
            params_list.append(data_dict)
        self.file.close()

        return params_list


if __name__ == "__main__":

    result = ReadDataDDT("VeehuiStudy_test.xlsx").getData()
    print(result)