# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/24 15:18
desc:对数据进行排序
"""

import pandas as pd
from pandas import DataFrame
import shutil
from collections import Counter
import numpy as np

pd.set_option('display.max_columns', 1000)  # 完全显示
pd.set_option('display.max_rows', None)  # 完全显示数据
data = pd.read_csv('data/all_question_answer_标注版_version_2021-11-04用于构建测试集.csv', encoding = 'utf-8').replace('\n', '')
# print('读取第一列', data['lable'])
data.sort_values('lable', ascending = False, axis = 0, inplace = True)
print('排序后的数据', data)

lable_list = list(data['lable'])

result = data.groupby('lable').head(1)  # 获取每一组的前3行数据
# print('抽取后的数据', res1)
# 把抽取出的数据每一组进行组内添加到列表，或者是把每一列中不同数据类型都提取出来，然后按照数据类型提取对应行的内容
result.to_csv('data/New1.csv', index= False, encoding = 'utf-8-sig')

'''
主要是为了组合数据

from itertools import combinations, combinations_with_replacement

for i in set(lable_list):
    content_list = []
    res2 = res1.loc[lable_data['lable'] == i]  # 获取对应i的行的内容
    res3 = res2['question']  # <class 'pandas.core.series.Series'>
    # content_list.append(res3)
    for j in res3:
        # print('抽取出来的数据：', j)  # 查看抽取出来的对应数据
        content_list.append(j)
    for answer in combinations(content_list, 2):
        # print('组合后的数据：', answer)  # 抽取组合后的数据类型是元组
        with open('data/new_construct_data.txt', 'a', encoding = 'utf-8') as recall:  # w改成a能持续写入文件，关闭程序不影响
            recall.write(str(answer) + '\n')  # 写入文档
print('处理完毕！')
'''
