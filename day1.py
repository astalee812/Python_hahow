# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:03:14 2020

@author: Asta Lee
"""
print(1+1)
print(1+2)

# 有個variable explorer可以看
a = 1

# 整數與浮點數
# 執行順序 - 一行一行執行出結果
print('第一個執行！')
print('第二個執行！')
print('第三個執行！')
print('第四個執行！')
print('第五個執行！')

# 變數
# 從variable explorer可以看到anyname是整數，test是浮點數
anyname = 1
anyname

test = 0.5
test

# 變數覆蓋
var = 10
var
var = 1.1
var

# 運算
a = 10
b = 3
c = a + b
c

c = a - b
c

c = a * b
c

c = a / b
c

c = a // b # 兩個除號是取"商"
c

c = a % b # %是取餘數
c

c = a ** b # 兩個*是平方的概念
c

#計算平均 (程式一樣有先乘除後加減的問題)
(1 + 5 +9 +100)/4

1 + 5 +9 +100/4

(1 + 78 +99 +100+101)/5

# 問題：
# 試著寫出求根公式
import math as math
a=1
b=4
c=4

x = (-b + math.sqrt((b**2)-4*a*c)) / 2*a
x

# 字串時間!!
# 給予值
anyname = '這是個字串' # 使用單引或雙引號都可以變成字串

# 字串相加
anyname2 = "商業分析"
anyname3 = anyname + anyname2
anyname3

# 看一下可不可以加減乘除都套用在字串上面
anyname4 = anyname - anyname2 # 減號不可以!
anyname4 = anyname * anyname2 # 相乘不可以!
anyname4 = anyname / anyname2 # 相除不可以!

# 不同型態串上 => 只有字串可以串字串，數字跟字串不可以相加
c = 10
g = anyname+ c

# 解法1
c = '10'
g = anyname+ c

# 解法2
c = '10'
g = anyname+ str(c)

# 取字串 => 這個很重要
# 切記 : python中的數字都是從0開始數
anyname3[2:7] # 抓第2個編號到第7個編號的字

anyname3[:7]

anyname3[2:]

anyname3[2:-7] # '-'是代表從後面開始數的意思