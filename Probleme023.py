# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:41:16 2016

@author: timothee.boulet
"""
import numpy as np

def sumProperDivisors(n):
    if n==1 or n==0:
        return 0
    result=[1]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            if i!=n/i :
                result.append(n/i)
    return sum(result)

def isAbundant(n):
    return sumProperDivisors(n)>n

def abundantNumbers(n):
    """Return all the abundant numbers below n"""
    seq = []
    for i in range(1,n+1):
        if isAbundant(i):
            seq.append(i)
    return seq

seq=abundantNumbers(28123)

canBe = []
for i, nb in enumerate(seq):
    for j in seq[i:]:
        add=nb+j
        if add not in canBe:
            canBe.append(nb+j)

canBe=sum(canBe[np.where(canBe<=28123)])
cannotBe=28123*28124/2-canBe

print(cannotBe)
    
