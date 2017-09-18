# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:02:30 2017

@author: ysyong
Largest prime factor
Problem 3 
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143 ?
"""

number = 100
factor = 2
factor_list = []

while number != 1:
    while number%factor == 0:
        number /= factor
        if factor not in factor_list:
            factor_list.append(factor)
    factor +=1

max_factor = max(factor_list)

print("The largest prime factor is", max_factor)