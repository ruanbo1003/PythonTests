# -*- coding:utf-8 -*-

import os
import uuid

import MySQLdb


db_ip = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = "123456"
dest_db_name = "test_db"


def delete_test_data():
    conn = MySQLdb.connect(host=db_ip, user=db_user, passwd=db_passwd, port=3306, db=dest_db_name, charset="utf8")
    cursor = conn.cursor()

    val = """this "is" a special 'value' test. """

    MySQLdb.escape_string(val)

    sql_str = f"""insert into t1(val) Values({val})"""
    print(sql_str)

    # conn.commit()
    #
    # cursor.close()
    # conn.close()

if __name__ == "__main__":
    delete_test_data()


