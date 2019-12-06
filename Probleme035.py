# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:44:20 2016

@author: timothee.boulet
"""

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True

final=[]

def isCircularPrime(n):
    if isPrime(n)==False:
        return False
    circularPrime=True
    seq = [nb for nb in str(n)]
    while circularPrime==True:  
        seq.append(seq[0])
        seq.remove(seq[0])
        temp=int(''.join(seq))
        if temp==n:
            return True
        if isPrime(temp)==False:
            return False
            
for i in range(1000000):
    if isCircularPrime(i):
        final.append(i)

print(len(final))
