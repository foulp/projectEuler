# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:17:17 2016

@author: timothee.boulet
"""

from operator import mul

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True


def primeDecomposition2(Limit):
    factors=[[1]]*(Limit+1)
    for i in xrange(2,Limit+1):
        if len(factors[i])==1: #isPrime
            k=2
            while k*i<=Limit:
                factors[k*i] = factors[k*i] + [i]
                k+=1
    return factors


limit=10**6
phi = primeDecomposition2(limit)
totient=[0.,1.,2.]
for n in xrange(3,limit+1):
    if isPrime(n):
        totient.append(n/float(n-1))
    else:
        totient.append(reduce(mul, [totient[k] for k in phi[n]], 1))

print(int(sum([round(float(n)/totient[n]) for n in range(2,limit+1)])))
