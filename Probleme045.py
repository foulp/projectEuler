# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:41:54 2016

@author: timothee.boulet
"""

def triangular(n):
    return n*(n+1)/2

def isPentagonal(n):
    temp=float(1+(1+24*n)**0.5)/6
    return temp==int(temp)
    
def isHexagonal(n):
    temp=float(1+(1+8*n)**0.5)/4
    return temp==int(temp)

current=286
while True:
    triangle=triangular(current)
    if isPentagonal(triangle) and isHexagonal(triangle):
        print(triangle)
        break
    current+=1
