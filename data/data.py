# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2020/11/11 17:03
# File: $ {NAME}
import sqlite3
class SetDataBase(object):
    def __init__(self,dataBaseName):
        self.conn = sqlite3.connect(dataBaseName)
        self.cursor = self.conn.cursor()
    def create_table(self,tableName):
        self.cursor.execute(f'create table {tableName} (id int primary key, name varchar(100), exp varchar(100))')
    def insert_values(self,tableName,id,body,exp):
        self.cursor.execute(f'insert into {tableName} values ({id},{body},{exp})')
    def select_table(self,tableName):
        self.cursor.execute(f'select * from {tableName}')
        value = self.cursor.fetchall()
        print(value)
    def close_cursor(self):
        self.cursor.close()
    def commit(self):
        self.conn.commit()
    def close_conn(self):
        self.conn.cursor()
if __name__ == '__main__':
    db = SetDataBase("userManager")
    # db.create_table("user001")
    db.insert_values("user","2","1","1")
    db.insert_values("user", "6","1", "1")
    db.commit()
    db.select_table("user")
    db.close_cursor()
    db.close_conn()

