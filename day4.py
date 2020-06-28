# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:15:22 2020

@author: Asta Lee
"""

# print 1~5
for i in [1,2,3,4,5]:
    print(i)

# 因為python開始值為0，所以結果是從0~4   
for i in range(5):
    print(i)
# 這邊才會變成1-5    
for i in range(5):
    print(i+1)    
        
# 設定範圍值，第5個是不會執行的
for i in range(1,5):
    print(i)    

# 設定範圍值以及公差
for i in range(1,5,2):
    print(i)
for i in range(-100,-5,2):
    print(i)

# 累加數值
count = 0
for i in [1,2,3,4,5]:
    count = i+count
    print(count)

# 問題：使用for迴圈，印出有tmr的句子(使用for迴圈來檢查每一個文章:可以用在爬蟲)
tmrlist = ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好']
for i in tmrlist:
    if 'TMR' in i :
        print(i)


# 問題：使用for迴圈與list，儲存有tmr的句子，爬蟲比較會用這個部分
tmrlist = ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好']
save = []
for i in tmrlist:
    if 'TMR' in i :
        print(i)
        save.append(i)

# while迴圈
c = 0
while c < 10:
    c = c + 1












    