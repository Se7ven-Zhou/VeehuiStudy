# coding :uff-8

class Environment:

    def __init__(self):

       pass

    def Test(self):
        ip = "http://apigw-dev.veehui.com"
        port = "80"
        url = ip + ":" + port
        return url

    def PreOnline(self):
        ip = "http://120.76.188.79"
        port = "9109"
        url = ip + ":" + port
        return url

    def Online(self):
        ip = "119.23.132.26"
        port = "8091"
        url = ip + ":" + port
        return url

if __name__ == "__main__":

    url = Environment().Test()
    print(url)