# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:31:15 2025

@author: DICT
"""


nums =  [10, 25, 30, 75, 160, 20, 5, 200, 15]

for num in nums:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)