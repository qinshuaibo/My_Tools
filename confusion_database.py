# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/11/12 17:06
desc: 从MySQL数据库中取出数据并进行打乱，然后切割为训练集和测试集
"""
import pandas as pd
import pymysql
import time

start = time.clock()  # 开始时间
''' 
# 连接数据库
db = pymysql.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'qa', port = 3306,
                     cursorclass = pymysql.cursors.DictCursor)
# db = MySQLdb.connect(host='localhost', user='qin', passwd='123', db='qa', cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()

cur.execute('select content from train_sentence;')
row = cur.fetchall()
print(row)
result = pd.read_sql_query(sql, cur)
'''
pd.set_option('display.max_columns', 1000)  # 完全显示
pd.set_option('display.max_rows', None)  # 完全显示数据

conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = '123456', db = 'qa')
result = pd.read_sql('select * from train_sentence', conn)
# print('数据类型：', type(result), result)  # result类型为dataframe
# result = pd.read_sql_query(sql, conn)
confusion_result = result.sample(1.0)
print('随机打乱之后的数据', confusion_result)
end = time.clock()  # 结束时间
