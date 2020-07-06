# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:09:53 2020

@author: Asta Lee
"""

# pandas 繪圖
"""
每張圖表都會有三大區塊
1. 載入函式庫
2. 輸入資料
3. 圖表設定參數
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
colors = ['#d9f776','#76f794','#9476f7','#f776d9','#76d9f7']
          
'''
載入資料集result
'''
result = pd.read_csv('result.csv')


# 直方圖
draw = result['sale']
draw.index = result['product']

# 直接把資料畫圖畫出來
draw.plot.bar() #line 、area
plt.ylabel("數量")
plt.xlabel("產品名稱") 
plt.title('各筆銷售概況') 
plt.show()

# 直方圖修改(plot.bar)
draw = result[['product','quantity','sale','price','cost']].groupby('product').sum()
draw.plot.bar(color=colors, stacked=False) #line 、area
plt.ylabel("數量",fontsize=15)
plt.xlabel("產品名稱",fontsize=15) 
plt.title('各產品銷售概況',fontsize=20) 
plt.show()

# 折線圖(plot.line)
draw.plot.line(color=colors)
plt.ylabel("數量",fontsize=15)
plt.xlabel("產品名稱",fontsize=15) 
plt.title('各產品銷售概況',fontsize=20) 
plt.show()

# 區域圖(plot.area) 
# (stacked = false 把線條以下的區域填滿)
draw.plot.area(color=colors, stacked=False)
plt.ylabel("數量",fontsize=15)
plt.xlabel("產品名稱",fontsize=15) 
plt.title('各產品銷售概況',fontsize=20) 
plt.show()


# 圓餅圖 (plot.pie)
draw.plot.pie(figsize=(30, 30),
              colors=colors,
              autopct='%.2f', # 加上浮點數 & 百分比
              fontsize=20,
              subplots=True)
plt.ylabel("數量",fontsize=15)
plt.xlabel("產品名稱",fontsize=15) 
plt.title('各產品銷售概況',fontsize=20) 
plt.show()



# 只想要銷售量的圓餅圖
draw = result[['product','sale']].groupby('product').sum()

draw.plot.pie(figsize=(10, 10),
              colors=colors,
              autopct='%.2f', 
              fontsize=20,
              subplots=True)
plt.ylabel("數量",fontsize=15)
plt.xlabel("產品名稱",fontsize=15) 
plt.title('各產品銷售概況',fontsize=20) 
plt.show()
