# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 08:57:20 2025

@author: DICT
"""


list1 = [10, 21, 30, 41, 50, 61]
list2 = [70, 81, 90, 101, 110, 121]

odd_idx = list1[1::2]
even_idx = list2[0::2]

res = odd_idx + even_idx

print(res)
