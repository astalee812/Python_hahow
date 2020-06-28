# -*- coding: utf-8 -*-
"""
Created on Tue May 19 00:37:01 2020

@author: Asta Lee
"""

# 比較符號
a = 3
b = 2

a > b 

a < b

# 兩個==是做比較，一個=是變數命名或指派
a == b

a != b

# 邏輯符號
not True

True and False 

True or True


# if 判斷式
# python 是以縮排為主的語言
a = 50
if a > 10:
    print('a 大於 10')
else:
    print('a 不大於 10')
    
# 判斷字串內是否（in）有"TMR"關鍵字 是就印出 YES!  否就印出NO
var = '今日頭條新聞，TMR公司開設行銷資料科學專班'
if 'TMR' in var:
    print('YES')    
else:
    print('NO')