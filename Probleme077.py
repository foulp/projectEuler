# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 14:22:39 2016

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



def numberOfWays(value, coins):
    ways=[0]*(value+1)
    ways[0]=1
    for coin in coins:
        for i in range(coin,value+1):
            ways[i]+=ways[i-coin]
    return ways[value]


n=1
while True:
    primes=[k for k in range(2,n-1) if isPrime(k)]
    total=numberOfWays(n, primes)
    if total>5000:
        print(n)
        break
    n+=1
