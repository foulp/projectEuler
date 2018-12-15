# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:42:19 2016

@author: timothee.boulet
"""

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True

somme=2
for i in range(3,2000000,2):
    if isPrime(i) :
        somme=somme+i
print(somme)