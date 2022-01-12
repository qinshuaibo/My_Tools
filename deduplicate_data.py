# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: 验证txt文档中按行写入列表并去重，保持原有顺序不变
"""

import pandas as pd
from pandas import DataFrame
from collections import Counter

data1 = pd.read_csv('E:/1_文件管理/a问答数据搜集/数据汇总/所有问题及答案汇总（处理版）.csv', 'r', encoding = 'utf-8', header = None)

lable_list = list(data1.iloc[:, 0].replace('\n', ' '))

print('数据长度', len(lable_list))  # 打印输出原始列表的长度

# 统计列表中每个元素数量
result = Counter(lable_list)

print('统计元素数量', result)
print('数据类型', type(result))

pd.set_option('display.max_columns', 1000)  # 完整显示pandas输出数据
pd.set_option('display.max_rows', None)
result1 = pd.value_counts(list)
print('统计元素数量', result1)

# 统计结果分析，数量低于7条的居然有500，这样的话，还得继续扩增，任务上不合理，太麻烦，干脆就这样得了

# 查找表格中重复的数据
read_data = pd.read_csv('E:/1_文件管理/a问答数据搜集/数据汇总/整理后的问题答案汇总版_v3_2021-11-17.csv.csv',
                        encoding = 'utf-8')  # , header = None
question_list = list(read_data.iloc[:, 1])  # .replace('\n', '')

print('数据长度', len(question_list))  # 打印输出原始列表的长度

from collections import Counter  # 引入Counter

b = dict(Counter(question_list))
# print([key for key, value in b.items() if value > 1])  # 只展示重复元素
print({key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数

# dict_name = []
# dict_pos = []
# dict_count = []
# with open('data/user_dict.txt', encoding = 'utf-8') as dict:
#     for line in dict.readlines():
#         dict_name.append(line.split()[0])
#         dict_pos.append(line.split()[0:1])
#         dict_count.append(line.split()[1:2])
#     print('字典长度', len(dict_name))
#     print('去重后字典长度：', len(set(dict_name)))
#     print('词性数量', len(dict_pos))
#     print('词频数量', len(dict_count))
# print(dict_name)
# print(set(dict_name))
#
# list_res = []
# for i in range(len(dict_name)):
#     list_res.append(dict_name[i], dict_pos[i], dict_count[i])  # 可以多个列表同时写入，如果列表长度相同的情况下，如list_res.append([a[i], list_cixing[i], value[i]])
#
# column_name = ['name', 'pos', 'count']  # 如果多个列可以在列表中增添列名，如column_name = ['人名', '地点', '时间']
# csv_name = 'data/txt_write_to_csv.csv'
# xml_df = pd.DataFrame(list_res, columns = column_name)
# xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
# print('写入完毕！')


test_list = [1, 1, 2, 3, 2, 3]  # 还是会出现io的问题
b = dict(Counter(test_list))
# b = dict(Counter(dict_name))
# print([key for key, value in b.items() if value > 1])  # 只展示重复元素
print('重复数据', {key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数
