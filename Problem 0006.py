# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:02:30 2017

@author: ysyong
Sum square difference
Problem 6 
    The sum of the squares of the first ten natural numbers is,
    
    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,
    
    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

"""
The most obvious way to solve the problem is using brute force as below. 
Just keep adding the number (natural or squared) to the sum to the last natural number.
From there, the difference is calculated.

This brute force method takes a longer time especially when a large number is involved
"""
import time
start = time.time()
naturalnumber = 10000000

sumofsquares = 0
sumofnumber = 0
for x in range(naturalnumber+1):
    sumofsquares += x**2
    sumofnumber += x

difference = sumofnumber**2 - sumofsquares

print("Difference between the sum of the squares and the square of the sum is", difference)
end = time.time()
print (end-start)

"""
An alternative is to use the two summation formula to calculate sum of natural number and sum of squared natural number
This is a lot faster as it takes a single formula (for both sums) and does not involve a loop
"""

start = time.time()
naturalnumber = 10000000

sumofnumber = naturalnumber*(naturalnumber+1)/2
sumofsquares = (2*naturalnumber+1)*(naturalnumber+1)*naturalnumber/6

difference = sumofnumber**2 - sumofsquares

print("Difference between the sum of the squares and the square of the sum is", difference)
end = time.time()
print (end-start)