# coding:utf-8

import os,time
from openpyxl import Workbook
from openpyxl import load_workbook


class WriteExcel:

    def __init__(self):

        self.address = self.address = os.path.split(os.path.dirname(__file__))[0] + "\Reports"
        self.report_name = time.strftime("%Y-%m-%d")+".xlsx"
        self.report_path = os.path.join(self.address,self.report_name)

    def creatExcel(self):

        if os.path.exists(self.report_path):
            pass
        else:
            ex = Workbook(self.report_path)     # 创建一个Excel
            sh = ex.create_sheet("result")     # 创建一个sheet
            ex.save(self.report_path)

            file = load_workbook(self.report_path)
            sheet = file.get_sheet_by_name("result")

            sheet.cell(row=1, column=1).value = "Name"
            sheet.cell(row=1, column=2).value = "Api"
            sheet.cell(row=1, column=3).value = "Params"
            sheet.cell(row=1, column=4).value = "Check"
            sheet.cell(row=1, column=5).value = "Response"
            sheet.cell(row=1, column=6).value = "Result"

            file.save(self.report_path)

    def writeErrorInfo(self,x,name,api,params,code,response,result = "False"):

        file = load_workbook(self.report_path)
        sheet = file.get_sheet_by_name("result")

        sheet.cell(row=x, column=1).value = name
        sheet.cell(row=x, column=2).value = api
        sheet.cell(row=x, column=3).value = params
        sheet.cell(row=x, column=4).value = code
        sheet.cell(row=x, column=5).value = response
        sheet.cell(row=x, column=6).value = result

        file.save(self.report_path)

    def getMaxRow(self):

        file = load_workbook(self.report_path)
        sheet = file.get_sheet_by_name("result")
        return sheet.max_row
        file.save(self.report_path)


if __name__ == "__main__":
    # name = 11
    # api = 22
    # params =33
    # code =44
    # response =55
    # WriteReport().Write_Report(name,api,params,code,response)
    x = WriteExcel().getMaxRow()
    print(x)
    print(type(x))