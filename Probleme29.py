# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:18:06 2016

@author: timothee.boulet
"""

As=list(range(2,101))
Bs=list(range(2,101))

seq=[]
for a in As:
    for b in Bs:
        temp=a**b
        if temp not in seq:
            seq.append(temp)
    
print(len(seq))