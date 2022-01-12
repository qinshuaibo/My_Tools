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
# data.sort_values('lable', ascending = False, axis = 0, inplace = True)
# print('排序后的数据', data)

np.random.seed(seed = 1)
gbr = data.groupby("lable")
gbr.groups
# print('分组后', gbr)

# lable_list = list(data['lable'])
# print('长度', len(lable_list))
# Dict = {}
# for key in lable_list:
#     Dict[key] = Dict.get(key, 0) + 1
# print('数据类型:', type(Dict), Dict)

# typicalDict = {'捕获特异性': '1', 'small RNA测序': '1', '覆盖率': '1', '测序深度数值': '1'}
data2 = pd.read_csv('data/NEW1.csv', encoding = 'utf-8', dtype = object,header = None)
lable_name = list(data2.iloc[:, 0])
lable_count1 = list(data2.iloc[:, 1])
print('标签数量', len(lable_name))
print('标签数量', len(lable_count1))
print(lable_name)
lable_count = []
for count in lable_count1:
    lable_count.append(int(count))
print(lable_count)

typicalDict = dict(zip(lable_name, lable_count))
print(typicalDict)


# sample = data.sample(frac = 0.1, random_state = 5, axis = 0)  # 只是按比例抽取,感觉容易出现数据不均匀的情况，因为
# print(sample)


# typicalDict1 = {1: 10, 2: 15}


def typicalsamling(group, typicalDict):
    name = group.name
    n = typicalDict[name]
    return group.sample(n = n)


result = data.groupby('lable').apply(typicalsamling, typicalDict)
# print(result.head())
result.to_csv('data/testdata.csv', index = False, encoding = 'utf-8-sig')

# print(data['lable'].value_counts())  # 查看各类型数量
