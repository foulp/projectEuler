# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 23:03:00 2017

@author: SansAccent
"""
import numpy as np

limit = 10**7

numbers = [{} for x in xrange(2,limit)]
factor = 1

for i,n in enumerate(numbers):
    if len(n)==0:
        a = i+2
        p = 1
        while a**p<limit:
            k = 1
            while k*a**p<limit:
                if p==1:
                    numbers[k*a**p-2][i+2] = 2
                else:
                    numbers[k*a**p-2][i+2] += 1
                k+=1
            p+=1
            
    numbers[i] = np.prod(numbers[i].values())
 
compteur, somme = 0, 0           
for i,n in enumerate(numbers[:-1]):
    if n==numbers[i+1]:
        compteur+=1
        somme+=i+2
