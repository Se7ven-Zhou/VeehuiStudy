# coding :utf-8

import requests
import HuShi.Config.SignatureConfig
from HuShi.Config.EnvironmentConfig import Environment
from HuShi.Common.PackageInfo import PackageInfo


class Login:

    def __init__(self,unionId,openId,accessToken,systemName = "Android|8681-A01;5.1;22"):

        self.openId = openId
        self.unionId = unionId
        self.accessToken = accessToken
        self.systemName = systemName

    def Login_APP(self,address):

        params = {}
        params["openId"] = self.openId
        params["unionId"] = self.unionId
        params["accessToken"] = self.accessToken
        params["systemName"] = self.systemName

        # 组装参数
        parameters = PackageInfo().packageParameter(str(params))

        api = "/u/loginByWechat"
        url = address + api

        post = requests.post(url,parameters)
        return post.json()


if __name__ == "__main__":
    address = Environment().Test()
    result = Login("o1WVZwxbvXmbZDgshqyxep4KhehE","owG8P08gTbda-maVestQIW9J50Og",HuShi.Config.SignatureConfig.accessToken).Login_APP(address)
    print(result)
