# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:19:44 2016

@author: timothee.boulet
"""

somme=0
for i in range(1,1001):
    somme+=(i**i)%10000000000
print(str(somme)[-10:])