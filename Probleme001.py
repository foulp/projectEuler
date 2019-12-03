# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:21:09 2016

@author: Timothée Boulet
"""
sum=0
for i in range(1000) :
    if i%3==0 or i%5==0 :
        sum+=i
print(sum)
