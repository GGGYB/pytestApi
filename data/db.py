# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2020/11/11 17:03
# File: $ {NAME}
import sqlite3
import pprint
class SetDataBase(object):
    def __init__(self):
        self.conn = sqlite3.connect("user")
        self.cursor = self.conn.cursor()
    def create_table(self,tableName):
        self.cursor.execute(f'create table {tableName} (id int primary key, url varchar(100), body varchar(100),exp varchar(100))')

    def insert_values(self,tableName,id,url,body,exp):
        self.cursor.execute(f"insert into {tableName} values ('{id}','{url}','{body}','{exp}')")

    # def update_values(self):
    #     self.cursor.execute(f"""update user set exp = '{"code":500,"msg":"Key:'userAddRequest.password'Error:Field validation for 'password' failed on the'required' tag"}' where id = 1""")
    def select_table(self,tableName):
        self.cursor.execute(f'select * from {tableName}')
        value = self.cursor.fetchall()
        pprint.pprint(value)
        print(value)
    def delete_value(self,tableName,id):
        self.cursor.execute(f'delete  from {tableName} where id = 1')
    def drop_db(self,dbName):
        self.cursor.execute(f'drop database {dbName}')
    def drop_table(self,tableName):
        self.cursor.execute(f'drop table {tableName}')
    def truncate_table(self,tableName):
        self.cursor.execute(f'truncate table {tableName}')
    def close_cursor(self):
        self.cursor.close()
    def commit(self):
        self.conn.commit()
    def close_conn(self):
        self.conn.cursor()
if __name__ == '__main__':
    db = SetDataBase()
    # db.create_table("user")
    db.insert_values('user','1','/api/v1/users','{"password":"","password_confirm": "88888888","username":"001"}',
                     '{"code":500,"msg":"userAddRequestpasswordError:Field validation for passwordfailed on therequiredtag"}')
    db.insert_values('user', '2', '/api/v1/users', '{"password":"55555","password_confirm":"88888888","username":"001"}',
                     '{"code": 500, "msg": "Key: userAddRequest.password Error:Field validation for password failed on the min tag"}')
    # db.update_values()
    db.commit()
    db.select_table("user")
    db.close_cursor()
    db.close_conn()

