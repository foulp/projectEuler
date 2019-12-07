# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 14:26:03 2016

@author: timothee.boulet
"""

a=str(28433)
j=7830457

for i in range(j):
    a=str(2*int(a))[-10:]
    
print(int(a)+1)
