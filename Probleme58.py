# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:43:40 2016

@author: Timothée Boulet
"""
def isPrime(n):
    if n in [2,3,5,7]: return True
    if n==1 or n%10 in [0,2,4,5,6,8]: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True
    
n=1
diag=1
compte=0
total=1
while True:
    while diag<n**2:
        diag+=n-1
        if isPrime(diag):
            compte+=1
        total+=1
    if compte<0.1*total and n>1:
        print(n)
        break
    n+=2

"""
Answer : 26241
"""
    