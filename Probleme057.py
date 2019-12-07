# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:26:33 2016

@author: timothee.boulet
"""

def next_square_root(a,b):
    return 2*b+a, a+b

compte=0
a=1
b=1
for n in range(1000):
    a,b=next_square_root(a,b)
    if len(str(a))>len(str(b)):
        compte+=1
print(compte)
