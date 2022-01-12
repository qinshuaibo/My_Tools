# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: csv文件转为json文件
"""

import csv
import json
import pandas as pd

with open('data/所有问题及答案汇总（标注版不带编号2021_10_21）.csv', 'r', encoding = "utf-8") as csvfile, \
        open('data/data.json', 'w', encoding = 'utf-8') as jsonfile:
    names = pd.read_csv('data/所有问题及答案汇总（标注版不带编号2021_10_21）.csv', encoding = 'utf-8', engine = 'python')
    # fieldnames = names.columns  # 获取列名
    fieldnames = ('lable', 'question_seg', 'question', 'answer')  # 获取列名
    for i in fieldnames:
        print(i)
    reader = csv.DictReader(csvfile, tuple(fieldnames))
    for row in reader:
        json.dump(row, jsonfile, ensure_ascii = False)  # 指定ensure_ascii=False 为了不让中文显示为ascii字符码
        jsonfile.write('\n')
print("succees!")
