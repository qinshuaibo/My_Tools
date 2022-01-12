# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: # 读取json文件
"""

import json


def read_corpus():
    '''从json文件中取出问题和答案'''
    question_seg_list = []
    question_list = []
    answer_list = []
    with open('data/data.json', encoding = 'utf-8') as f:
        for line in f:
            question_seg = json.loads(line)['question_seg']
            question = json.loads(line)['question']
            answer = json.loads(line)['answer']
            question_seg_list.append(question_seg)
            question_list.append(question)
            answer_list.append(answer)
            # print(question, type(question))
        # print(len(question_seg_list), type(question_seg_list))
        # print(len(question_list), type(question_list))
        # print(len(answer_list), type(answer_list))
    assert len(question_list) == len(answer_list)
    return question_list, answer_list

read_corpus()

question_list, answer_list = read_corpus()

print(question_list[20000],question_list[40000])  # 在列表中索引还是比较快的

word_dict = {}
with open('data/user_dict.txt', encoding = 'utf-8') as dict:
    for line in dict.readlines():
        # print(line)
        key = line.split(' ')[0]
        # print(key)
        value = line.split(' ')[1:2]
        # print(type(value))
        for i in value:
            word_dict[key] = str(i)
print(type(word_dict))

# print(word_dict[key])

inverted_idx = {}
# 将关键词添加到倒排表中
for key, value in word_dict.items():
    # print(key,value)
    if int(value) > 0 and int(value) < 10000:
        inverted_idx[key] = []
print(inverted_idx['瑞研安'])

