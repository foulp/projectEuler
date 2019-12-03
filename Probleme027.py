# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 02:01:18 2016

@author: Timothée Boulet
"""

def isPrime(n):
    if n<2:
        return False
    if n in [2,3,5] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] or n%3==0 : 
        return False
    for i in range(7,int(n**0.5)+1, 2):
        if n%i==0 :
            return False
    return True
    

def numberOfPrime(a,b):
    index=0
    current=b
    while isPrime(current) :
        index+=1
        current=index**2+a*index+b
    return index

best=0
a_max=-1000
b_max=-1000
for a in range(-999,1000) :
    for b in range(-999,1000) :
        temp=numberOfPrime(a,b)
        if temp>best:
            best=temp
            a_max=a
            b_max=b
            
print(a_max, b_max)
