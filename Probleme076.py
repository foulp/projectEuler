# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:28:01 2016

@author: timothee.boulet
"""

d=100
ans=[1]+[0]*d

for j in range(1,d+1):
    for i in range(j, d+1):
        ans[i]+=ans[i-j]

print(ans[d]-1)
