# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:34:44 2019

@author: Ivan
"""
# --------Sales of Child Car Seats--------
#介紹資料
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 讀資料
datas = pd.read_csv('carseats.csv')

##各式圖表
#Bar charts 

# 建立資料
names = ['蘋果', '橘子', '檸檬', '柳橙']
values = [10, 56 ,5 ,20]

plt.bar(names, values)
plt.show()

# 問題：
## 長條圖實戰：境外與境內的分店個數
# 取出各境內境外資料
InUS = datas[datas['US'] == 'Yes']
OutUS = datas[datas['US'] == 'No']

# ['In US','Out US']
names = ['In US','Out US']
values = [InUS['US'].count(), OutUS['US'].count()]

plt.bar(names, values)
plt.title('分店數量')
plt.xlabel('地點')
plt.ylabel('數量')
plt.show()


#Pie charts
# 建立資料
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs'] #標籤值
sizes = [15, 30, 45, 10] #各標籤比例
explode = [0.3, 0.1, 0, 0] # 移開的距離

# pie（各比例, 移開, 標籤, 數值格式, 陰影, 轉向角度）
plt.pie(sizes, explode = explode, labels=labels,
        autopct='%1.1f%%', shadow=True,startangle=90 )
# 讓圓餅圖畫出來是圓形
plt.axis('equal')  
plt.show()


# 問題：
##圓餅圖實戰：境外與境內的分店比例
# 建立資料境內境外之料
InUS = datas[datas['US']=='Yes']
OutUS = datas[datas['US']=='No']

# hint:pd.unique
labels =['In US','Out US']#取出獨立標籤
sizes = [len('In US'),len('Out US')] #各標籤比例
explode = [0.1,0] 

plt.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.axis('equal')  
plt.title('境內外比例')
plt.show()


#Scatter plots 散佈圖
# 建立資料

x = [1,2,3,4,2,3,4,3,5,5]
y = [5,5,6,7,10,2,7,10,8,5]
size =[70,20,100,20,30,50,30,50,60,70]
color = [1,2,3,4,1,2,3,4,1,2]
plt.scatter(x, y, s = size,c = color)
plt.show()


#散佈圖實戰：價格  銷量 境外 
# 取出境內靜外的dataframe
InUS = datas[datas['US']=='Yes']
OutUS = datas[datas['US']=='No']

# 抓出境內(InUS)的Price 與Sales
# 然後畫出帶有label = Yes的散佈圖
InUS.head()

x1 = InUS['Price']
y1 = InUS['Sales']
plt.scatter(x1, y1)
plt.show()

# 抓出境外(OutUS)的Price 與Sales
# 然後畫出帶有label = No的散佈圖
x2 = OutUS['Price']
y2 = OutUS['Sales'] 
plt.scatter(x2, y2)

# 畫圖
plt.title('價格分布')
plt.xlabel('價格')
plt.ylabel('銷售')
plt.legend()
plt.show()
