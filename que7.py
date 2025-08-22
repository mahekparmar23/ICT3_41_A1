# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:06:31 2025

@author: DICT
"""


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ch_size = len(l) // 3

ch1 = l[:ch_size][::-1]
ch2 = l[ch_size:2*ch_size][::-1]
ch3 = l[2*ch_size:][::-1]

res = [ch1, ch2, ch3]
print(res)