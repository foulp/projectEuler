# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 18:57:01 2016

@author: Timothée Boulet
"""
def isPrime(n):
    if n in [2,3,5,7]: 
        return True
    if n==1 or n%10 in [0,2,4,5,6,8]: 
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: 
            return False
    return True
    

limit = 50*10**6    
primes=[2]+[n for n in range(3,int(limit**0.5)+1,2) if isPrime(n)]
primes3=[n for n in primes if n<=int(limit**(1/3.))+1]
primes4=[n for n in primes3 if n<=int(limit**0.25)+1]


previous=[]
for a in primes:
    print(a)
    for b in primes3:
        for c in primes4:
            test=a**2+b**3+c**4
            if test<=limit:
                previous.append(test)

print(len(set(previous)))
    