# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:18:27 2020

@author: Asta Lee
"""

# 介紹pandas : 專門處理二維資料(dataframe)! 做資料清理
import pandas as pd

# 製作dataframe，將dictionary直接轉成dataframe
data = {'uid':[1,2,3,4,5],
        'name':['Jack','Lily','Kevin',
                'Jojo','Harry'],
        'age':[25,21,35,18,15]}
member = pd.DataFrame(data)
member

# 把資料前5筆資料印出來
member.head()

# 看欄位資訊，這邊很像R的str()
member.info()

# 修改欄位名稱
test = member
test.columns
test.columns = ['num', 'word', 'fix']
test.columns

# 更改欄位名稱之後，可以看到先前的資料欄位也改變了
test
member

# 如果不想要一起被修改，就要加上copy
test = member.copy()
test.columns
test.columns = ['num', 'word', 'fix']
test.columns

member = pd.DataFrame(data)
member

# 取得一欄或多欄資料
# df['columname']
member['name']

# 多個欄位使用list包起來
member[['name', 'age']]

# 與上面的相同，不同用法做出相同的結果
colname = ['name', 'age']
member[colname]

colname = ['uid', 'age']
member[colname]

member[['uid', 'age']]

# 常見計算
member['age']

member['age'].mean()
member['age'].max()
member['age'].min()
member['age'].describe() # 這邊會像r的summary

# 排序
member['age'].sort_values()
member['age'].sort_values(ascending = False)

# 刪除欄位
member.drop(columns = ['uid', 'age'])

# 將所有值轉回陣列
member.values.tolist()

# 整欄資料型別轉換
member['age'] = member['age'].astype('float64')
member['age'] 

member['age'] = member['age']
member['age'] .astype('int')

member.to_csv('member.csv',encoding='utf-8-sig')






