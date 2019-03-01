# coding = utf-8


import pymysql
import HuShi.Config.MySqlConfig

class InitializeDada:

    def __init__(self):

        self.db_ip = HuShi.Config.MySqlConfig.ip
        self.db_port = HuShi.Config.MySqlConfig.port
        self.db_tableName = HuShi.Config.MySqlConfig.tableName
        self.db_username = HuShi.Config.MySqlConfig.username
        self.db_pwd = HuShi.Config.MySqlConfig.password

    def initData(self,sql,datas=None):
        try:
            conn = pymysql.Connect(self.db_ip,self.db_username,self.db_pwd,self.db_tableName,self.db_port,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
        except:
            conn.close()

        # 创建游标
        cousor = conn.cursor()
        try:
            cousor.execute(sql)
            conn.commit()
            print("************** 初始化账号成功 **************")
        except:
            conn.rollback() # 事务回滚

        conn.close()


if __name__ == "__main__":
    SQL = "select id from user_info where id=58"
    CleanData().initData(SQL)
