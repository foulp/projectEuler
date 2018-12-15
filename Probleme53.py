# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:48:04 2016

@author: Timothée Boulet
"""
def fact(n):
    if n<=1:
        return 1
    return fact(n-1)*n

factorielle = [fact(n) for n in range(101)]

def comb(n,r, factorielle):
    return factorielle[n]/factorielle[r]/factorielle[n-r]

compte=0   
for n in range(101):
    for r in range(n+1):
        if comb(n,r, factorielle)>=10**6:
            compte+=1

print(compte)

"""
Answer : 4075
"""