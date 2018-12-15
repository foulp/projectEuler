# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:39:49 2016

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

def isSumOfConsecutivePrimes(n, primes):    
    current=n
    length=0
    while current>0:
        for prime in primes[primes<current]:
            test=current-prime
            if test in primes:
                length+=1
                current=test
                break
            return False            
    return length

primes=[i for i in range(1000000) if isPrime(i)]