# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/2/8 14:23
desc:对txt文档添加编号
"""
import sys
import os

sys.path.append('../..')
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

file = open("../data/target.txt", 'r', encoding = 'utf-8')
lines = file.readlines()
# print(lines)

n = 0
with open("../data/target.txt", 'a+', encoding = 'utf-8')as f:
    for line in lines:
        f.write(str(n) + ' ' + line)
        # print(line)
        n = n + 1
