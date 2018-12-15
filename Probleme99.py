# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 14:32:06 2016

@author: timothee.boulet
"""
from math import log

f=open("C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme99_base_exp.txt")
lines=f.read().split('\n')
exp = [[int(line.split(',')[0]),int(line.split(',')[1])] for line in lines]

best=log(exp[0][0])*exp[0][1]
i_best=0
limit=1000
for i in range(1,limit):
    a , b = exp[i][0] , exp[i][1]
    test=b*log(a)
    if test>best :
        best=test
        i_best=i
    
print(i_best+1) #Numero de la ligne