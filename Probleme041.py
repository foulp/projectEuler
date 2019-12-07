# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:25:52 2016

@author: timothee.boulet
"""
from itertools import permutations

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True

def isPandigital(n):
    seq=[nb for nb in str(n)]
    if len(seq)==9 and all(str(k) in seq for k in list(range(1,10))):
        return True
    else:
        return False

best=0       
for n in range(9,1,-1):
    if best!=0:
        break
    seq = list(range(1,n+1))
    temp=[]
    for element in permutations(seq):
        temp.append(int(''.join([str(el) for el in element])))
    for number in temp[::-1]:
        if isPrime(number):
            best=number
            break

print(best)
