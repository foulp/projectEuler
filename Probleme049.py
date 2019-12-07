# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:22:56 2016

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

def isPermutation(a,b):
    sa, sb = str(a), str(b)
    if sa==sb or len(sa)!=len(sb):
        return False
    for letter in sa:
        if letter not in sb:
            return False
    for letter in sb:
        if letter not in sa:
            return False
    return True
    

for i in range(1001,9998):
    if isPrime(i):
        for k in range(2,(9999-i)/2+1,2):
            if isPrime(i+k) and isPrime(i+2*k) and isPermutation(i,i+k) and isPermutation(i,i+2*k):
                start, increment = i,k
                break
print(int(''.join([str(start), str(start+increment), str(start+2*increment)])))
