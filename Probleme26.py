# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:50:13 2016

@author: Timothée Boulet
"""
i_max=0
maximum=0

for i in range(1000,1,-1):
    if maximum>=i:
        break
    
    remains=[]
    remain = 10%i
    while remain not in remains and remain!=0:
        remains.append(remain)
        remain = remain*10%i

    if remain==0:
        current=0
    else:
        temp=remains.index(remain)
        current=len(remains)-temp
    
    maximum=max(maximum, current)
    i_max=i

print(i_max)
        