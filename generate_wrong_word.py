# -*- coding:utf-8 -*-
"""
Author:秦帅波
Time:2021/12/23 14:49
File:generate_wrong_word.py
Version:Python 3.7.10
IDE:PyCharm
Desc: 生成同音不同字，可以用来构建错别字
"""
import pypinyin
from pypinyin import lazy_pinyin
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
dagParams = DefaultDagParams()
word = '瑞化安'
pinyin_list = lazy_pinyin(word)
result_word = dag(dagParams, pinyin_list, path_num=10, log=True)  #
print(result_word)

'''
 def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag
    dagParams = DefaultDagParams()
    result = dag(dagParams, pinyinList, path_num=10, log=True)#10代表侯选值个数
    for item in result:
        socre = item.score
        res = item.path # 转换结果
        print(socre, res)
if __name__ == '__main__':
    lists1 = ['jing', 'chang']
    pinyin_2_hanzi(lists1)
    '''