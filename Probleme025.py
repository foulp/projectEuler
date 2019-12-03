# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 01:52:05 2016

@author: Timothée Boulet
"""

def first_fibo(n) :
    seq=[1,1]
    while len(str(seq[-1]))<1000:
        seq.append(seq[-2]+seq[-1])
    return len(seq)
        
        
print(first_fibo(1000))
        
