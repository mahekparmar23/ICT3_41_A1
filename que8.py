# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:19:35 2025

@author: DICT
"""


lst =  [1, 2, 1, 3, 2, 3, 1, 2]
    
count_dict = {}

for i in  lst:
    if i in count_dict:
        count_dict[i] += 1 
    else:
        count_dict[i] = 1
        
print(count_dict)
