# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:32:07 2016

@author: timothee.boulet
"""

from fractions import gcd

limit=12000
compte=0

for d in range(3,limit+1):
    for n in range(int(d/3.)+1, int(d/2.)+1):
        if gcd(n,d)==1:
            compte+=1
            
print(compte)
