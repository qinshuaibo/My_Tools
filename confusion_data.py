# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/11/12 17:06
desc: 从表格中取出数据并进行打乱
"""
import pandas as pd
import pymysql
import time

pd.set_option('display.max_columns', 1000)  # 完全显示
pd.set_option('display.max_rows', None)  # 完全显示数据

data = pd.read_csv('data/train_write_to_csv.csv', encoding = 'utf-8')
print('类型', type(data))
confusion_data1 = data.sample(frac = 1)
# print('随机打乱之后的数据', confusion_data1)
train_data = data.sample(frac = 0.7)
# print('切分出来的训练数据70%', train_data)
dev_data = confusion_data1[~confusion_data1.index.isin(train_data.index)]
print('剩下的数据作为测试数据', dev_data)

# 重新写入表格
# 如果多个列可以在列表中增添列名，如column_name = ['人名', '地点', '时间']
# train_column_name = ['question', 'label_ids']
# csv_name = 'data/dev_write_to_csv.csv'
# xml_df = pd.DataFrame(dev_data, columns = train_column_name)
# xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
# print('写入完毕！')

# 重新写入表格
# 如果多个列可以在列表中增添列名，如column_name = ['人名', '地点', '时间']
test_column_name = ['question', 'label_ids']
csv_name = 'data/train_new_write_to_csv.csv'
xml_df = pd.DataFrame(train_data, columns = test_column_name)
xml_df.to_csv(csv_name, encoding = 'utf-8-sig', index = None)
print('写入完毕！')

# 计时
start = time.clock()  # 开始时间
end = time.clock()  # 结束时间
cost_time = end - start
print('耗时：', cost_time)
