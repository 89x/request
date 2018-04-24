import pymysql
import configparser
import json
class OpenMysql:
    def __init__(self):
        self.coon = pymysql.connect(
            host="100.114.31.253",
            port ="3306",
            user="artsfetch",
            password = "artsfetchpassword",
            db = "ishop",
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.coon.cursor()
    def search_one(self,sql):
        self.cur.execute(sql)
        results = self.cur.fetchall()
        return results


if __name__ == '__main__':
	op_mysql = OpenMysql()
	print(op_mysql.search_one("select * from tb_user where id = 320187"))