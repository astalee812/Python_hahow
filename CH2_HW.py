# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:49:09 2020

@author: Asta Lee
"""
# HW for CH2

import pandas as pd

# 問題：匯入檔案purchase_list.csv
transaction = pd.read_csv('purchase_list.csv')

transaction.info()
transaction.columns
# 這邊我想看product上面有幾種資料
set(transaction['product'])

'''
資料篩選
'''
# 問題：請篩選出所有香蕉的資料
set(transaction['product'])
banana = transaction[transaction['product']=='banana']
banana


'''
整欄計算 + - * /
'''
# 問題：計算每筆交易的總額（購買量＊單價），並存到'total'欄位中
transaction['total'] = transaction['quantity'] * transaction['price']
transaction.head()

'''
群組計算 groupby
'''
# 問題：列出五種水果的總銷售量。
transaction[['product','total']].groupby('product').sum()


'''
切分群組
'''
# 問題：依照欄位'total'的大小，區分成["小額消費", "正常消費", "鉅額消費"]，並儲存在'priceclass'欄位中。
transaction['priceclass'] = pd.cut(transaction['total'],3,
       labels=["小額消費", "正常消費", "鉅額消費"])
transaction

'''
對照合併 merge
'''
productCost = {'product':['origin', 'apple', 'guava', 'banana', 'cherry'],
        'cost':[1,3,10,15,41]
        }
productCost = pd.DataFrame(productCost)

# 問題：依照欄位'product'合併資料表productCost與transaction
result = pd.merge(transaction, productCost, 
                  how='left', on=['product'])

result.head()

'''
存檔
'''
# 問題：請將Dataframe變數result存檔
result.to_csv('result.csv',encoding='utf-8')