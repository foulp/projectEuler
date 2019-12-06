# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:21:06 2016

@author: timothee.boulet
"""

def isPowerWritten(n,p):
    if n==1:
        return False
    somme=0
    for nb in str(n):
        somme+=int(nb)**p
    if somme==n:
        return True
    else:
        return False

seq=[]
for i in range(1000000):
    if isPowerWritten(i,5):
        seq.append(i)
print(sum(seq))
