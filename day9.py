# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:40:00 2020

@author: Asta Lee
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


 datas = pd.read_csv('carseats.csv')
 
x = datas['Population']
y = datas['Sales']

# 畫圖! 人口跟銷量之間的關係(一開始會產生沒有相關)
fig, ax = plt.subplots(figsize=(10, 8)) #調整軸的大小
ax.scatter(x,y)
plot.show

Baddata = datas[datas['ShelveLoc'] =='Bad']
x_B = Baddata['Population']
y_B = Baddata['Sales']

Gooddata = datas[datas['ShelveLoc'] =='Good']
x_G = Gooddata['Population']
y_G = Gooddata['Sales']

Meddata = datas[datas['ShelveLoc'] =='Medium']
x_M = Meddata['Population']
y_M = Meddata['Sales']

# 圖二 (把三個圖疊在一起)
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, label = 'Bad')
ax.scatter(x_G, y_G, label = 'Good')
ax.scatter(x_M, y_M, label = 'Medium')
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
plt.show()

# 這邊要把自然流量從0變成1，不然會是0
Size_B = Baddata['Advertising'] +1
Size_G = Gooddata['Advertising']+1
Size_M = Meddata['Advertising']+1

# 圖三
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, s=Size_B*5, label = 'Bad')
ax.scatter(x_G, y_G, s=Size_G*5, label = 'Good')
ax.scatter(x_M, y_M, s=Size_M*5, label = 'Medium')
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
plt.title('Advertising budget')
plt.xlim(0,530) #設定x軸顯示範圍
plt.ylim(0,17) #設定y軸顯示範圍
plt.xlabel('Population')
plt.ylabel('Sales')
plt.show()










