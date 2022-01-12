# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/12/13 11:00
desc:利用近义词文件构建近义词字典
"""
import synonyms

# while True:
#     user_input = input("请输入：\n")
#     print(synonyms.display(user_input))
#     with open('data/relate_words/relate_test.txt', 'a', encoding = 'utf-8') as test:
#         test.write(str(synonyms.display(user_input)) + '\n')

for line in open('data/user_dict2.txt', 'r', encoding = 'utf-8'):
    item = line.split(" ")
    word = item[0]
    print(word, synonyms.nearby(word, 10)[0])  # display数据类型为NoneType,nearby数据类型为tuple,里面元素为列表，在这里直接输出第一个元素
    # for i in synonyms.nearby(word, 10):
    #     print(word, i)  # i数据类型为列表
    with open('data/relate_words/test.txt', 'w', encoding = 'utf-8') as test:
        for text in synonyms.nearby(word, 10)[0]:
            test.write(word + text)  # TODO 写入文件

"""
def generate_related_words(file):
    '''
    建立相关词汇字典
    file:相关词汇文件所在路径
    '''
    dict_related = {}
    for line in open(file, mode = 'r', encoding = 'utf-8'):
        item = line.split(",")
        word = item[0]
        a = synonyms.display(word)
        # si_list = [value for value in item[1].strip().split()]
        # dict_related[word] = si_list
    return a


related_words = generate_related_words('../data/relate_words/related_words.txt')

print("related_words", related_words)

# print('对应的所有值', '数据类型', type(related_words.values()), related_words.values())
"""
