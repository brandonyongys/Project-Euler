# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:05:20 2017

@author: ysyong
Self powers
Problem 48 
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
    
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
import time
start = time.time()

limit = 1000
total = 0
for i in range(1,limit+1):
    total += i**i

total_str = str(total)
Last10digits = total_str[-10:]

print("The last 10 digits are", Last10digits)
end = time.time()
print(end - start)