# coding : utf-8

import time
import requests

class PackageInfo:

    def __init__(self):

        pass

    def packageParameter(self,params = {},token = "",signature = "",admin = "!QS#$^Tghi0"):
        parameters = {}
        parameters["admin"] = self.admin
        parameters["signature"] = signature
        parameters["timestamp"] = int(time.time()*1000)
        parameters["params"] = params
        parameters["token"] = token

        return parameters


    def packageErrorMessage(self,result_code,right_code,result):
        error_info = "<AssertionError> " + result_code + "≠" + right_code + " <Response:\t" + result + ">"

        return error_info

if __name__ == "__main__":
    url = "http://119.23.132.26:8092/meeting/getLive"
    parameter = PackageInfo().packageParameter()

    post = requests.post(url,parameter)
    print(post.json())
