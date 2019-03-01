# coding = utf-8

import time,os

class GetLatestReport:

    def getLatestPath(self):
        address = os.path.split(os.path.dirname(__file__))[0] + "\Reports"
        # 当前文件名以时间排序成列表
        dir_list = os.listdir(address)
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(address, x)))
        latestReportPath = address + "/" + dir_list[-2]

        return latestReportPath

if __name__ == "__main__":

    path = GetLatestReport().getLatestPath()
    print(path)
    file_name = os.path.split(path)[1]
    print(file_name)
