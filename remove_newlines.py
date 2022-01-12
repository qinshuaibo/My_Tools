# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/12/9 18:24
desc:去掉单元格中的换行符
"""
import pandas as pd

data = pd.read_csv("F:/没有答案的问题/没有答案的问题.csv")

col = ["label", "question"]
new_f = data[col].replace('\\n', ' ', regex = True)
new_f.to_csv("F:/没有答案的问题/没有答案的问题去掉空格.csv", index = False, encoding = 'utf-8-sig')
print("处理完毕！")
