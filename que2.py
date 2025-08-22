# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 08:24:54 2025

@author: DICT
"""

start = 1
end = 11
prev_num = 0

for start in range(start,end):
    sum = start + prev_num
    print(f"{start} + {prev_num} = {sum}")
    prev_num = start    