# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:38:49 2016

@author: Timothée Boulet
"""


small=2520
found=False
while found==False:
    if small%3==0 and small%7==0 and small%8==0 and small%9==0 and small%11==0 and small%13==0 and small%16==0 and small%17==0 and small%19==0:
        found=True
    else :
        small+=20

print(small)
