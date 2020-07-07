# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:13:16 2020

@author: Asta Lee
"""

# matplotlib = 基礎2D畫圖，可以畫統計跟數學的東西! 可塑性很高!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 這邊是把字體從font.sans-serif換成Microsoft JhengHei 
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# 解決座標軸負數的負號顯示問題
plt.rcParams['axes.unicode_minus'] = False


# base 
plt.plot([1,2,3,4])
plt.xlabel('數字')
plt.show

# 多加點資料進去 (x,y)
x = [1,2,3,4]
y = [4,8,12,16]
plt.plot(x,y)
plt.xlabel('數字')
plt.show

# 使用dataframe的資料丟進去看看
# 結果會有兩條線會自己跑出來!
data = pd.DataFrame([{'a':1,'b':3},{'a':2,'b':4}])
data
plt.plot(data)
plt.xlabel('數字')
plt.show()

# lable title
# 0-2之間要挑選出30個資料
x = np.linspace(0, 2, 30)
plt.plot(x, x**3)
plt.title('大標題') #加入標題
plt.xlabel('x標籤') #加x軸標籤
plt.ylabel('y標籤') #加y軸標籤
plt.show()

# plt.axis 設定軸範圍
x = np.linspace(0, 2, 30)
plt.plot(x, x**3)
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.xlim(0,2.5) #設定x軸顯示範圍(0~2.5)
plt.ylim(0,9) #設定y軸顯示範圍(0~9)

# plt.axis 設定刻度
x = np.linspace(0, 2, 30)
plt.plot(x, x**3)
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.xlim(0,2.5) #設定x軸顯示範圍
plt.ylim(0,9) #設定y軸顯示範圍
#產生刻度陣列(npArray 類式list)
tick_arr = np.arange(0,2.5,0.2) # 在0~2.5之間每0.2就畫一個刻度
plt.xticks(tick_arr) #設定刻度
plt.yticks([]) #空值代表隱藏刻度
plt.show()

# Marks
# https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
x = np.linspace(0, 2, 30)
plt.plot(x, x**3,'-o') #第三個參數設定記號(ppt no.14有詳細的記號)
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.xlim(0,2.5)
plt.ylim(0,9)
plt.show()

# Grid = 貼加格線! 讓點點比較好對應到刻度
x = np.linspace(0, 2, 30)
plt.plot(x, x**3,'-o') #第三個參數設定記號
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.xlim(0,2.5)
plt.ylim(0,9)
plt.grid(True) # grid 開啟
plt.show()

# muti line = 畫很多條線
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o') #設定第一條折線圖
plt.plot(x, x**2)  #設定第二條折線圖
plt.plot(x, x**3)  #設定第三條折線圖
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.show()

# 結合直方& 直線
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o') #設定第一條折線圖
plt.plot(x, x**2)  #設定第二條折線圖
plt.bar(x, x**3)  #設定第三條折線圖
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 

# legend = 圖例
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='線性') #給予線標籤
plt.plot(x, x**2, label='平方') #給予線標籤
plt.plot(x, x**3, label='次方') #給予線標籤
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.legend() #開啟圖例
plt.show()


# legend2 圖例為子
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='線性') #給予線標籤
plt.plot(x, x**2, label='平方') #給予線標籤
plt.plot(x, x**3, label='次方') #給予線標籤
plt.title('大標題') 
plt.xlabel('x標籤') 
plt.ylabel('y標籤') 
plt.legend(loc =7) #開啟圖例(最多到11)
plt.show()

# seaborn 配色很漂亮的套件，但是可塑性很低，有些東西沒辦法自己調

import seaborn as sns 

purchase_list= pd.read_csv('purchase_list.csv', encoding='utf-8')
purchase_list.info()
purchase_list.head()

#設定圖片為中文
sns.set(font='sans-serif')
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

#柱狀圖（比例） -- sns.barplot 這邊會顯示比例的
ax = sns.barplot(x = "gender", 
                 y = "牛奶", 
                 data = purchase_list
                 ).set_title("牛奶顧客分類-性別")

#合併柱狀圖（比例）
ax = sns.barplot(x="recency_cate", 
                 y="牛奶", 
                 hue="gender", # 合併柱狀圖
                 data=purchase_list
                 ).set_title("牛奶購買頻率分類-性別")

#柱狀圖（數量） -- sns.countplot 實際數量為何
ax = sns.countplot(x="牛奶"
                   , data=purchase_list
                   ).set_title("牛奶單次購買的數量")

#柱狀圖（橫向）
ax = sns.countplot(y='牛奶',
                   data=purchase_list,
                   hue='gender'
                   ).set_title("牛奶單次購買的數量")

#點線圖
ax = sns.factorplot(x="orderdate", 
                    y="牛奶", 
                    data=purchase_list[:10])#kind = 'bar,swarm,violin,box'
ax.set_xticklabels(rotation=30) # 把字轉了30度
ax.fig.suptitle('牛奶購買狀況（日）')

#曲線圖
ax = sns.kdeplot(purchase_list["recency"],shade=True)#cumulative=True,vertical=True
ax = sns.kdeplot(purchase_list[purchase_list["recency"]>30]["recency"],label='good')
ax = sns.kdeplot(purchase_list[purchase_list["recency"]<31]["recency"],label='bad').set_title("距離上次購買天數")

#kdeplot圖片劃分 : 最後要指定哪個圖要放在哪個畫布
fig,axes=plt.subplots(1,3) # 這邊用畫布切割
ax = sns.kdeplot(purchase_list["recency"],shade=True,ax=axes[0]).set_title("距離上次購買天數")#cumulative=True,vertical=True
ax = sns.kdeplot(purchase_list[purchase_list["recency"]>30]["recency"],label='good',ax=axes[1]).set_title("距離上次購買天數")
ax = sns.kdeplot(purchase_list[purchase_list["recency"]<31]["recency"],label='bad',ax=axes[2]).set_title("距離上次購買天數")

#FacetGrid圖片劃分
#柱狀圖
ax = sns.FacetGrid(purchase_list, col="gender")
ax.map(plt.hist, "牛奶")




















