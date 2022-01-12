# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: 利用倒排索引进行查找，这个文件已经没必要，
"""

import json
from collections import Counter
import jieba


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
print(len(question_list))

word_dict = {}
with open('data/user_dict_test.txt', encoding = 'utf-8') as dict:
    for line in dict.readlines():
        # print(line)
        key = line.split(' ')[0]
        # print(key)
        value = line.split(' ')[1:2]
        # print(type(value))
        for i in value:
            word_dict[key] = str(i)
# print(word_dict)

inverted_idx = {}  # 定一个一个简单的倒排表
# 将关键词添加到倒排表中
for key, value in word_dict.items():
    if int(value) > 0 and int(value) < 10000:
        inverted_idx[key] = []
# print('倒排表类型', type(inverted_idx))
# print(inverted_idx)  # 现在字典对应的值还是空的

'''
print('结巴分词类型', type(jieba.cut('瑞研安产品介绍')))  # 结巴分词后的数据类型为generator

def cut(input_list):  # 主要是结巴分词参数是列表，我觉得应该改为句子字符串
    list_new = []
    # list_new = list(jieba.cut(str(input_list)))
    for sentence in input_list:
        seg = jieba.cut(sentence)
        list_new.append(seg)
    # list_new.append(jieba.cut(str(input_list)))
    # list_new.append(str(i))
    return list_new


# 在倒排表中添加关键词存在于qlist中的索引
keywords_index = 0
for q in cut(question_list):
    # print('分词后的问题',q)
    for word in q:
        # print(word)
        if word in inverted_idx.keys():
            inverted_idx[word].append(keywords_index)
    keywords_index += 1
# print('添加问题后的倒排索引', inverted_idx)
# print('添加问题后的倒排索引值', inverted_idx.keys())

list11 = ['瑞研安', '瑞泰康']  # cut函数是对列表进行分词，所以输入得是列表

idx_list = []
for i in list11:
    print(i)
    if i in inverted_idx.keys():
        print('对应的句子', i, inverted_idx[i])
        print('依次对应的索引长度', len(inverted_idx[i]))
        idx_list += inverted_idx[i]
    print('总的索引长度', len(idx_list))

for idx in list(set(idx_list)):
    print('question:', question_list[idx], 'answer:', answer_list[idx])
'''


def cut1(input):  # 主要是结巴分词参数是列表，我觉得应该改为句子字符串
    list_new = []
    # list_new = list(jieba.cut(str(input_list)))
    # for i in jieba.cut(input):
        # list_new.append(i)
    list_new += list(jieba.cut(input))
    # list_new.append(jieba.cut(str(input_list)))
    # list_new.append(str(i))
    return list_new


# 在倒排表中添加关键词存在于qlist中的索引
keywords_index = 0
for sentence in question_list:
    # print(sentence)
    for word in cut1(sentence):
        # print('分词后的问题', q)
        # for word in q:
            # print(word)
        if word in inverted_idx.keys():
            inverted_idx[word].append(keywords_index)
    keywords_index += 1
# print('添加问题后的倒排索引', inverted_idx)
# print('添加问题后的倒排索引值', inverted_idx.keys())

list12 = cut1('瑞研安，瑞泰康，基因，基因检查')
# list12 = ['瑞研安', '产品', '功能']
print('经过cut1处理后的类型', type(list12))
print('分词后', list12)

idx_list = []
for i in list12:
    print(i)
    if i in inverted_idx.keys():
        print('对应的句子', i, inverted_idx[i])
        print('依次对应的索引长度', len(inverted_idx[i]))
        idx_list += inverted_idx[i]
print('总的索引长度', len(idx_list))

for idx in list(set(idx_list)):
    print('question:', question_list[idx], 'answer:', answer_list[idx])

'''
# TODO: 基于倒排表的优化。在这里，我们可以定义一个类似于hash_map, 比如 inverted_index = {}，
#  然后存放包含每一个关键词的文档出现在了什么位置，
#       也就是，通过关键词的搜索首先来判断包含这些关键词的文档（比如出现至少一个），然后对于candidates问题做相似度比较。
#
import numpy as np

# 将qlist转换为句子向量
qlist_matrix = []
for q in question_list:
    q_vec = get_words_vec(q)
    qlist_matrix.append(q_vec)

qlist_matrix = np.asarray(qlist_matrix)


def top5results_emb(input_q):
    """
    给定用户输入的问题 input_q, 返回最有可能的TOP 5问题。这里面需要做到以下几点：
    1. 利用倒排表来筛选 candidate
    2. 对于用户的输入 input_q，转换成句子向量
    3. 计算跟每个库里的问题之间的相似度
    4. 找出相似度最高的top5问题的答案
    """

    abs_v = abs(qlist_matrix[0])
    # 存储所有返回结果的索引
    res = []
    # 从倒排表中取出相关联的索引
    index_list = []
    for c in cut([input_q]):
        for i in c:
            if i in inverted_idx.keys():
                index_list += inverted_idx[i]
    index_list = list(set(index_list))
    # input_q的vec值
    input_q_vec = get_words_vec(input_q)
    # 遍历倒排表内所有值，将list中所有vec值与input_q的vec值做对比，绝对值差较小的数的索引存入res中
    for value in qlist_matrix[index_list]:
        if abs(input_q_vec - value) < abs_v:
            abs_v = abs(input_q_vec - value)
            res.append(qlist_matrix[index_list].tolist().index(value))

    top_indx = np.argsort(res)[-5:].tolist()

    return answer_list[top_indx]
'''
