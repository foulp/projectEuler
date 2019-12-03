# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:18:57 2016

@author: timothee.boulet
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(40)/fact(20)**2)
