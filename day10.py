# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 00:42:59 2020

@author: Asta Lee
"""

import pandas as pd
from Ivan_ptt import crawl_ptt_page


## 必要設定的欄位
# 1. 修改ptt板位
# 2. 查看最新的頁數index
KoreaDrama = crawl_ptt_page(Board_Name ='KoreaDrama' ,
                            start =2366 ,page_num= 5)
creditcard = crawl_ptt_page(Board_Name ='creditcard' ,
                            start =3336 ,page_num= 5)

# 這邊匯出的資料在excel打開會是亂碼，但是可以先用記事本開啟，接著另存新檔，點選還有BOM的UTF-8覆蓋檔案即可
KoreaDrama.to_csv('KoreaDrama_test.csv',encoding = 'utf-8') #存檔

creditcard.to_csv('creditcard_test.csv',encoding = 'utf-8') #存檔


aa = pd.read_csv('KoreaDrama_test.csv',encoding = 'utf-8')
bb = pd.read_csv('creditcard_test.csv',encoding = 'utf-8')