# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:20:02 2016

@author: timothee.boulet
"""

from itertools import permutations

seq=list(range(0,10))
temp=[]
for element in permutations(seq):
    digits=[str(el) for el in element]
    if int(''.join(digits[1:4]))%2==0:     
        if int(''.join(digits[2:5]))%3==0:
                if int(''.join(digits[3:6]))%5==0:
                        if int(''.join(digits[4:7]))%7==0:
                                if int(''.join(digits[5:8]))%11==0:
                                        if int(''.join(digits[6:9]))%13==0:
                                            if int(''.join(digits[7:]))%17==0:
                                                    temp.append(int(''.join(digits)))

print(sum(temp))

