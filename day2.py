# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:23:17 2020

@author: Asta Lee
"""

# 陣列
a = [1,2,3,4,5]

# 要切記! 編號是從0開始編號
a[0]

# 取出List資料
a[4]

# 計算長度
print(len(a))

# 常見操做
a.append(7) # 加入數字7到a陣列中
a.append(9)
a.append(5) # 加入數字5到a陣列中
a
a.sort() # 排序
a

# 雙重陣列
c = ['123',['456','789']]
c[1]
c[1][1]


# 等於也算是一個陣列
d = '你好嗎'
d[0]


# Dictionary : 都是用中括號包起來，1個key對應一個value
# 可以新增無限多筆資料! 類似json
dic = {'key1':'Value1',
       'key2':'Value2',
       'key3':'Value3',
       'getme': 'Yooooooooooo~'}

# 取出Dictionary資料
dic['key2']

# 問題
# 嘗試取出 'Yooooooooooo~'
dic['getme']


# dictionary裡面可以再包一個dictionary
# key可以使用數字
{'key1':'Value1',
   'key2':'Value2',
   'key3':'Value3',
   'key4': {'key1':'Value1',
           'key2':'Value2',
           'key3':'Value3',
           'key4': 'Value4'}}














