# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:23:35 2016

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
    
def isTruncatable(n):
    seq = [nb for nb in str(n)]
    
    for i in range(len(seq)):
        if isPrime(int(''.join(seq[:i+1])))==False:
            return False
            
    for i in range(len(seq)):
        if isPrime(int(''.join(seq[i:])))==False:
            return False
            
    return True

start=11
final=[]
while len(final)<11:
    if isTruncatable(start):
        print(start)
        final.append(start)
    start+=2

print(sum(final))

