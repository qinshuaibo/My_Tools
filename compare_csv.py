# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/12/7 17:03
desc:对文件中同一行的两列相同内容标为1，主要是处理标注数据
"""
import pandas as pd

# 读取数据
pd_reader = pd.read_csv('E:/1_文件管理/a问答数据搜集/测试Top标注/B_answer(1).csv', encoding = 'utf-8')
list_question = list(pd_reader.iloc[:, 0])
list_question_1 = list(pd_reader.iloc[:, 1])
list_question_2 = list(pd_reader.iloc[:, 2])
list_question_3 = list(pd_reader.iloc[:, 3])
list_question_4 = list(pd_reader.iloc[:, 4])
list_question_5 = list(pd_reader.iloc[:, 5])

column_name = ['lable']  # 如果多个列可以在列表中增添列名，如column_name = ['人名', '地点', '时间']
csv_name = 'E:/1_文件管理/a问答数据搜集/测试Top标注/B_answer(1)1.csv'
# xml_df = pd.DataFrame(list_res, columns = column_name)
# xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
# print('写入完毕！')

lable_list = []
for i, a, b, c, d, e in zip(list_question, list_question_1, list_question_2, list_question_3, list_question_4,
                            list_question_5):

    if i == a:
        lable1 = 1
        # print('与第一列相同的')
        print(i, a, lable1)  # 只有6564个
        lable_list.append(lable1)
        # xml_df = pd.DataFrame(lable1_list, columns = ['lable'])
        # xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
    else:
        lable0 = 0
        # print('与第一列不相同的')
        print(i, a, lable0)
        lable_list.append(lable0)
print(lable_list)
print('长度', len(lable_list))
xml_df = pd.DataFrame(lable_list, columns = ['lable'])
xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
'''
    if i == b:
        lable2 = 2
        print('与第二列相同的')
        print(i, b, lable2)  # 只有180个
    if i == c:
        lable3 = 3
        print('与第三列相同的')
        print(i, c, lable3)  # 只有20个
    if i == d:
        lable4 = 4
        print('与第四列相同的')
        print(i, d, lable4)  # 只有5个
    if i == e:
        lable5 = 5
        print('与第五列相同的')
        print(i, e, lable5)  # 只有5个
'''