# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:56:53 2016

@author: timothee.boulet
"""

def isPandigital(n):
    seq=[nb for nb in str(n)]
    if len(seq)==9 and all(str(k) in seq for k in list(range(1,10))):
        return True
    else:
        return False

final=[]
for i in range(10000):
    seq=[]
    if i<10:
        for j in range(1,10):
            seq.append(str(i*j))
            temp=int(''.join(seq))
            if i>=2 and isPandigital(temp):
                final.append([temp, i, j])         
    if 10<=i<100:
        for j in range(1,5):
            seq.append(str(i*j))
            temp=int(''.join(seq))
            if i>=2 and isPandigital(temp):
                final.append([temp, i, j])
    if 100<=i<1000:
        for j in range(1,4):
            seq.append(str(i*j))
            temp=int(''.join(seq))
            if i>=2 and isPandigital(temp):
                final.append([temp, i, j])
    if 1000<=i:
        for j in range(1,3):
            seq.append(str(i*j))
            temp=int(''.join(seq))
            if i>=2 and isPandigital(temp):
                final.append([temp ,i, j])
    
print(max([triple[0] for triple in final]))
