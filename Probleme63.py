# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:37:28 2016

@author: timothee.boulet
"""
n=1
while True:
    n+=1
    if len(str(9**n))<n:
        break
compte=0
for i in range(1,n):
    for j in range(1,10):
        if len(str(j**i))==i:
            print(j,i, j**i)
            compte+=1

print(compte)