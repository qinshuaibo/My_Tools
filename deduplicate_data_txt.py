# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 17:15
desc: 删除txt文本中重复行
"""
list = []
with open('E:/easy_qa/QA-System-master/data/stopword_list/stopwords_index_all.txt', 'r', encoding = 'utf-8') as read, \
        open('E:/easy_qa/QA-System-master/data/stopword_list/new.txt', 'a', encoding = 'utf-8') as writefile:
    for line in read.readlines():
        # print(line)
        list.append(line)
    print('去重之前的数量', len(list))
    lines_seen = set()  # Build an unordered collection of unique elements.
    print('去除重复数据后的长度', len(lines_seen))
    # for line in read:
    #     line = line.strip('\n')
    #     if line not in lines_seen:
    #         writefile.write(line + '\n')
    #         lines_seen.add(line)

with open('E:/easy_qa/QA-System-master/data/stopword_list/stopwords_index_all.txt', 'r',
          encoding = 'utf-8') as read1, \
        open('E:/easy_qa/QA-System-master/data/stopword_list/new.txt', 'r',
             encoding = 'utf-8') as read2:
    a_list = []
    b_list = []
    for line in read1.readlines():
        # print(line)
        a_list.append(line)
    for line in read2.readlines():
        # print(line)
        b_list.append(line)
for i in a_list:
    if i not in b_list:
        print(i)