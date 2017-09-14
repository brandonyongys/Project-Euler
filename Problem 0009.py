# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:36:44 2017

@author: Brandon Yong
Special Pythagorean triplet
Problem 9 
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    
    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""
import math

s = 1000
limit = math.ceil(s/3+1)
for a in range(1,limit):
    b = ((s**2)/2-s*a)/(s-a)
    if b%1 == 0:
        c = s - a - b
        break

print("The values of a, b, c are %s, %s and %s" %(a,int(b),int(c)))
print("The product of the Pythagorean triplet is", int(a*b*c))


