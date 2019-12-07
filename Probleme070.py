# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:02:54 2016

@author: timothee.boulet
"""

from operator import mul


def areAnagrams(str1, str2):
    #If the lengths are different they're not anagrams !
    n1=len(str1)
    n2=len(str2)
    if n1!=n2:
        return 0
        
    # Sort both strings
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
 
    # Compare sorted strings
    for i in xrange(n1):
        if str1[i] != str2[i]:
            return 0 
    return 1

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


limit=10**7
phi = primeDecomposition2(limit)
totient=[0.,1.,2.]
best=10**4
n_best=0
for n in xrange(3,limit):
    if isPrime(n):
        totient.append(n/float(n-1))
    else:
        totient.append(reduce(mul, [totient[k] for k in phi[n]], 1))
        
    if areAnagrams(str(n), str(int(round(n/totient[n])))) and best>totient[n]:
        best=totient[n]
        n_best=n

print(n_best)

