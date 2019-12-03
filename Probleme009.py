# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:26:31 2016

@author: timothee.boulet
"""

def isPythagoreanTriplet(a,b,c) :
    if a>=b or b>=c :
        return False
    if a**2+b**2==c**2 :
        return True
    else :
        return False

for c in range(1001) :
    for b in range(c+1) :
        a=1000-b-c
        if a>=0 and isPythagoreanTriplet(a,b,c) :
            print(a,b,c)
            print(a*b*c)
            break
