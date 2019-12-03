# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:56:57 2016

@author: timothee.boulet
"""

def fact(n) :
    if n==2:
        return 2
    else:
        return n*fact(n-1)

def sumDigits(n):
    return sum([int(nb) for nb in str(n)])
    
print(sumDigits(fact(100)))
