# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:00:47 2016

@author: timothee.boulet
"""
def sumDiago(n):
    if n==1:
        return 1
    return sumDiago(n-2)+2*(n**2+(n-2)**2+n-1)

print(sumDiago(1001))
    
    
