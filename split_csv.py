# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: 对csv文件进行分割，方便打开
"""

import pandas as pd
from pandas import DataFrame

file_name = r'E:/1_文件管理/a问答数据搜集/数据汇总/经过整理的数据/核心业务数据/疾病套餐靶点靶向药.csv'  # 获取待处理文件路径名称

import chardet

f = open(file_name, 'rb')
lines = f.readline()
file_code = chardet.detect(lines)['encoding']

with open(file_name, 'r', encoding = file_code) as f:
    csv_file = f.readlines()
    linesPerFile = 200  # 定义分割行数
    filecount = 1  # 初始化文件编号
for i in range(0, len(csv_file), linesPerFile):
    with open(file_name[:-4] + '_' + str(filecount) + '.csv', 'w+', encoding = 'utf-8-sig') as f:
        if filecount > 1:
            f.write(csv_file[0])

        f.writelines(csv_file[i: i + linesPerFile])
        filecount += 1

# 计算耗时多长
import time

st = time.time()
et = time.time()
cost_time = et - st
print('处理完成，程序运行时间：{}秒'.format(float('%.2f' % cost_time)))
