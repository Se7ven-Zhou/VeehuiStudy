# coding:utf-8

import pymysql
import HuShi.Config.MySqlConfig

class ConnectSQL:

    def __init__(self):

        self.db_ip = HuShi.Config.MySqlConfig.ip
        self.db_port = HuShi.Config.MySqlConfig.port
        self.db_tableName = HuShi.Config.MySqlConfig.tableName
        self.db_username = HuShi.Config.MySqlConfig.username
        self.db_pwd = HuShi.Config.MySqlConfig.password

    def connectMySQL(self,sql,datas=None):
        try:
            conn = pymysql.Connect(self.db_ip,self.db_username,self.db_pwd,self.db_tableName,self.db_port,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
        except:
            conn.close()

        # 创建游标
        cousor = conn.cursor()
        try:
            rows = cousor.execute(sql)
        except:
            conn.rollback() # 事务回滚

        conn.close()

        return cousor.fetchone()

if __name__ == "__main__":
    sql = "SELECT SUM(coin_num) as result FROM user_operation_record WHERE user_id=77777 AND coin_num>1"
    result = ConnectSQL().ConnectMySQL(sql)
    print(str(result["result"]))
