# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: 删除表格中重复行
"""

import pandas as pd
from pandas import DataFrame
import shutil

data = pd.read_csv('E:/1_文件管理/a问答系统数据/原始问答数据整理/all_question_answer_标注版_version_2021-11-04.csv', encoding = 'utf-8')  # , engine = 'python'
sentence_list = list(data.iloc[:, 2].replace('\n', ' '))
print('数据长度', len(sentence_list))
print('去重后的数据长度', len(set(sentence_list)))

# 完全显示
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', None)

# 查看基于某一列去除重复行的结果
# frame = pd.read_csv('data/删除重复行.csv', engine = 'python')
drop_data = data.drop_duplicates(subset = ['question'], keep = 'first', inplace = False)
# print('去除重复行之后的数据', drop_data)

# 写入表格数据
drop_data.to_csv('E:/1_文件管理/a问答系统数据/原始问答数据整理/all_question_answer_标注版_version_2021-11-04去重版.csv', index = False, encoding = 'utf-8-sig')
