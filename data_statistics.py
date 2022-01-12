# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/7/9 14:15
desc:
"""
import pandas as pd

'''
# 读取数据
pd_reader = pd.read_csv(r'data/train.csv', encoding = 'utf-8', header = None)
list_train_question_1 = list(pd_reader.iloc[:, 0])
list_train_question_2 = list(pd_reader.iloc[:, 1])

print('训练数据中第一列数量', len(list_train_question_1))
print('训练数据中第二列数量', len(list_train_question_2))

pd_reader = pd.read_csv(r'data/test.csv', encoding = 'utf-8', header = None)
list_test_question_1 = list(pd_reader.iloc[:, 0])
list_test_question_2 = list(pd_reader.iloc[:, 1])

# print(test_question1)
print('测试数据中第一列数量', len(list_test_question_1))
print('测试数据中第二列数量', len(list_test_question_2))

pd_reader = pd.read_csv(r'data/dev.csv', encoding = 'utf-8', header = None)
list_dev_question_1 = list(pd_reader.iloc[:, 0])
list_dev_question_2 = list(pd_reader.iloc[:, 1])

print('验证数据中第一列数量', len(list_dev_question_1))
print('验证数据中第二列数量', len(list_dev_question_2))

repeat_sentence = []
for sentence in list_dev_question_1:
    if sentence in list_train_question_1:
        repeat_sentence.append(sentence)

print('不重复的数据', len(repeat_sentence))
# 验证集中与训练集不重复9399，重复601，说明是没有切分直接进行
# 测试数据跟训练集重复的567+621 + 531 + 574，测试集与验证集也181，说明切分的时候不是完全切分的
'''

data1 = pd.read_csv(r'E:/1_文件管理/a问答数据搜集/数据汇总/临时1.csv', encoding = 'utf-8')

data_list1 = list(data1.iloc[:, 0].replace('\n', ' '))

# data2 = pd.read_csv(r'E:/1_文件管理/a问答数据搜集/数据汇总/整理后的问题答案汇总版_v4_2021-11-19.csv', encoding = 'utf-8', header = None)

data_list2 = []
for line in open('data/user_dict2.txt', 'r', encoding = 'utf-8'):
    item = line.split(" ")
    word = item[0]
    data_list2.append(word)
print('字典中长度：', len(data_list2))
# data_list2 = list(data2.iloc[:, 0].replace('\n', ' '))

data = data_list1 + data_list2
print('合并之后去重的数量', len(data))

duplicate_data1 = []
for i in data_list1:
    if i not in data_list2:
        duplicate_data1.append(i)
        print(i)
print('在list1中不在list2的', len(duplicate_data1))

duplicate_data2 = []
for j in data_list2:
    if j not in data_list1:
        duplicate_data2.append(j)
        print(j)

print('在list2中不在list1的', len(duplicate_data2))

all_data = duplicate_data1 + duplicate_data2
print('去重后的数据', len(set(all_data)))
