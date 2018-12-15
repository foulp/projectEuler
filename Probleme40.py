# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:19:15 2016

@author: timothee.boulet
"""
champernowne='0'
i=1
while len(champernowne)<=1000000:
    champernowne+=str(i)
    i+=1

print(int(champernowne[1])*int(champernowne[10])*int(champernowne[100])*int(champernowne[1000])*int(champernowne[10000])*int(champernowne[100000])*int(champernowne[1000000]))