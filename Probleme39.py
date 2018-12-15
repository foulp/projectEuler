# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:57:11 2016

@author: timothee.boulet
"""

def isRightAngleTriangle(a,b,c):
    seq=[a,b,c]
    seq.sort()
    if seq[0]**2+seq [1]**2==seq[2]**2:
        return True
    else:
        return False

final={}
for p in range(4,1001):
    final[p]=0
    for c in range(int(p/3)+1 ,p-1):
        for b in range(1,int((p-c)/2+1)):
            a=p-b-c
            if a<=c and b<=c:
                if isRightAngleTriangle(a,b,c):
                    final[p]+=1

print(max(final, key=final.get))