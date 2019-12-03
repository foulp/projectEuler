# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:44:49 2016

@author: Timothée Boulet
"""

def isPrime(n):
    if n in [2,3,5] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] or n%3==0 : 
        return False
    for i in range(7,int(n**0.5)+1, 2):
        if n%i==0 :
            return False
    return True

def largestPrimeFactor(n) :
    result = 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0 :
            if isPrime(i):
                result=i
            test=int(n/i)
            if isPrime(test)==True:
                return test
    return result
    
print(largestPrimeFactor(600851475143))
