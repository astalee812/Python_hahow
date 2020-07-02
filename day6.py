# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:14:00 2020

@author: Asta Lee
"""

import pandas as pd

transaction = pd.read_csv('transaction.csv')

# 條件式會回傳每一個列位的T or F
transaction['product'] == 'apple'

# 將條件式裡面的T or F中只挑選T出來
transaction[transaction['product'] == 'apple']

# 只顯示T0003的交易數據
transaction[transaction['tid'] == 'T0003']

# 整欄計算
transaction['quantity'] * transaction['price']

# 將資料轉為類別型態
pd.get_dummies(transaction['product'])

# 群組切分 cut(切割的資料,分成幾等分,要替換的標籤)
# 這邊沒有做儲存，也不會在原資料內加這欄
pd.cut(transaction['price'],3,
       labels = ['cheap', 'medium','expensive'])
# solve: (這邊會有相同欄位的問題)
priceclass = pd.cut(transaction['price'],3,
       labels = ['cheap', 'medium','expensive'])

# concat : 合併資料!! axis = 1 (左右合併); axis = 0(上下合併)
# concat有點像是不依照key值去做合併
newdata = pd.concat([transaction, priceclass], axis = 1)

# 還有另外一種方式 : 這個是直接創一個新欄位然後把資料塞進去
transaction['price_cut'] = pd.cut(transaction['price'],3,
                           labels = ['cheap', 'medium','expensive'])

# groupby分群計算，要記得要加sum!
transaction.groupby('product').sum()
transaction.groupby('tid').sum()

# 只計算特定欄位
name = ['product', 'quantity']
transaction[name].groupby('product').sum()
transaction[name].groupby('product').mean()

# Q: 如何計算總業績
transaction['sale'] = transaction['price'] * transaction['quantity']

# Q: 計算每個商品的總業績
name = ['product', 'sale']
transaction[name].groupby('product').sum()

# 對照合併: merge
member = pd.read_csv('member.csv')

# merge : how(left, right, inner, outer); on = key value
pd.merge(transaction, member,
         how = 'left', on = ['uid'])

# 計算每個使用者的銷售量
result = pd.merge(transaction, member,
         how = 'left', on = ['uid'])

result[['name', 'sale']].groupby('name').sum()

# 刪除重複資料 drop.duplicates
transaction.drop_duplicates('tid')

# 根據條件取row and colum
# 隨機取兩欄出來(前row後colum)
transaction.iloc[::, 0:2]
transaction.iloc[0:2,::]
transaction.iloc[0:2,0:2]