# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:56:31 2016

@author: timothee.boulet
"""
from fractions import gcd

a=0
b=1
best=0
for d in range(1,10**6+1):
    for n in range(int(d*best), int(d*3./7)+1):
        temp=float(n)/d
        if gcd(n,d)==1 and temp<3./7 and temp>best:
            a,b=n,d
            best=temp
    
print(a, b, best, 3./7)