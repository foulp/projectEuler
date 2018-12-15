# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:29:44 2016

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

def isComposite(n):
    if n==1 or isPrime(n):
        return False
    return True
    
def okConj(n):
    for i in range(1,int((n/2-1)**0.5)+1):
        if isPrime(n-2*i**2):
            return True
    return False
                

current=33
found=False
while found==False:
    if current%100000==1:
        print(current)
    current+=2
    if isPrime(current)==False:
        if okConj(current)==False:
            found=True

print(current)