# coding:utf-8

from wxpy import *
import time


class SentWeChat:

    def __init__(self,name = "HS",groupNanme = "叽叽喳喳"):

        self.bot = Bot(cache_path=True)
        self.friend = self.bot.friends().search(name)[0]
        self.time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.group = self.bot.groups().search(groupNanme)[0]

    def  systemError(self,api):
        message = "["+ self.time + "]接口:" + api + "系统异常"
        self.friend.send(message)
        self.group.send(message)

    def noService(self,api):
        message = "["+ self.time + "]接口:" + api +  "无服务"
        self.friend.send(message)

    def logicError(self,api):
        message = "["+ self.time + "]接口:" + api +  "逻辑错误"
        self.friend.send(message)

if __name__ == "__main__":
    SentWeChat().systemError("/api/login")

