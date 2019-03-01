# coding:utf-8

import time,os
from openpyxl import load_workbook
from openpyxl import Workbook
from urllib import request
from prettytable import PrettyTable
from HuShi.Common.GetLatestReport import GetLatestReport
from pyquery import PyQuery as pq


class MailInfo:

    def __init__(self):

       self.path =  GetLatestReport().getLatestPath()

    def getErrorData(self):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        para_list = []
        for i in range(2, sheet.max_row + 1):
            pass
            data_list = []
            for j in range(1, sheet.max_column + 1):
                data = sheet.cell(row=i, column=j).value
                data_list.append(data)
            para_list.append(data_list)

        file.close()

        x = PrettyTable(["name", "api", "result"])
        for i in range(len(para_list)):
            x.add_row(para_list[i])

        return (str(x))


    def getInfo(self, count, testTime, tester="Seven"):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        count_fail = int(sheet.max_row) - 1
        count_pass = int(count) - int(count_fail)

        if int(count_fail) == 0:
            count_passRate = 1
        else:
            count_passRate = int(count_pass) / int(count)

        info = ("""<div class='heading'>
<h1 style="font-family: Microsoft YaHei">VeehuiStudy_API</h1>
<p class='attribute'><strong>测试人员 : </strong> Seven</p>
<p class='attribute'><strong>测试时间 : </strong>{}</p>
<p class='attribute'><strong>合计耗时 : </strong> {:.2f}秒</p>
<p class='attribute'><strong>测试结果 : </strong> 共 {}，通过 {}，失败 {}，通过率= {:.2%}</p>
<p class='description'></p>
</div>""".format(time.strftime("%Y-%m-%d %H:%M:%S"),testTime, count, count_pass, count_fail, count_passRate))

        file.close()

        return info


if __name__ == "__main__":
    path = "C:/Users/Administrator/PycharmProjects/pythonStudy/venv/HuShi/Reports/2018-10-24.xlsx"
    # test = Package_MailContent(path).test_info(5)
    # print(test)
    info = MailInfo().getInfo(5,1.2333)
    print(info)
