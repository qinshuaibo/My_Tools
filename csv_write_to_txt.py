# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/24 15:18
desc:csv文件中数据依次写入txt不同的列，中间用空格隔开
"""

import pandas as pd
from pandas import DataFrame
import numpy as np

# a = []
# with open('data/new_construct_data.txt', 'r', encoding = 'utf-8') as QA:
#     for i in QA:
#         a.append(i)
# print('问题数量长度', len(a))
#
# list_res = []
# for i in range(len(a)):
#     list_res.append(a[i])  # 可以多个列表同时写入，如果列表长度相同的情况下，如list_res.append([a[i], list_cixing[i], value[i]])
#
# column_name = ['人名']  # 如果多个列可以在列表中增添列名，如column_name = ['人名', '地点', '时间']
# csv_name = 'data/txt_write_to_csv.csv'
# xml_df = pd.DataFrame(list_res, columns = column_name)
# xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
# print('写入完毕！')


import csv

out = open('data/new_construct_data.csv', 'w', newline = '', encoding = 'utf-8-sig')
csv_writer = csv.writer(out, dialect = 'excel')

with open('data/new_construct_data.txt', 'r', encoding = 'utf-8') as QA:
    for line in QA.readlines():
        line = line.replace(',', '\t')
        list = line.split()
        csv_writer.writerow(list)





