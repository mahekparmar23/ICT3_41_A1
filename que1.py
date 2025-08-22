# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 08:11:22 2025

@author: DICT
"""

def product(a, b):
    prod = a * b
    if prod > 1000:
        return a + b
    else:
        return prod

print(product(10, 20))
print(product(50, 25))