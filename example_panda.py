# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/12/7 10:33
desc:
"""
import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine

# 连接数据库
connection = pymysql.connect(host = 'localhost',
                             port = 3306,
                             user = 'qin',
                             password = '123',
                             db = 'qa',
                             charset = 'utf8',
                             cursorclass = pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# cursor.execute('select * from train_sentence;', cursor)  # 查询语句
# row = cursor.fetchall()

# 读取sql
data_sql = pd.read_sql("select sentence1, sentence2, lable from train_sentence", connection)
print(type(data_sql), data_sql)  # 数据属性DataFrame

# 打乱数据
df = data_sql.sample(frac = 1.0)  # d
df = df.reset_index(drop = True)

print('随机打乱后的数据', df)

# 切分数据 训练集 测试集 验证集
train = df.iloc[:4200000]
print(train)

# # 存储
# data_sql.to_csv("test.csv")

'''
# 用sqlalchemy构建数据库链接engine
db_info = {'user': 'qin',
           'password': '123',
           'host': 'localhost',
           'database': 'qa'  # 这里我们事先指定了数据库，后续操作只需要表即可
           }

engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,
                       encoding = 'utf-8')  # 这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。

sql_cmd = "SELECT * FROM train_sentence "  # 语句：从train_sentence表格中读取数据
df = pd.read_sql_query(sql = sql_cmd, con = engine)
print(type(df), df)
# pandas.read_sql(sql, con, index_col = None, coerce_float = True, params = None, parse_dates = None, columns = None,
#                 chunksize = None)
'''
