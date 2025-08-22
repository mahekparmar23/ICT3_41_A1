# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:37:16 2025

@author: DICT
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 10
end = 50

print(f"Prime numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number, end=' ')
