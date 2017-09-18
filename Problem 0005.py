# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:05:20 2017

@author: ysyong
Smallest multiple
Problem 5 
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
start = time.time()

import numpy as np

number = 100
limit = 20
factors = np.arange(1,limit + 1)

while all(number % factors == 0) != True:
    number += 10

print("The smallest positive number that is evenly divisible by all of the numbers form 1 to 20 is",number)
end = time.time()
print(end - start)