# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 02:45:07 2016

@author: Timothée Boulet
"""
import numpy as np

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
   
result=[]

for i in range(10,100):
    for j in range(i+1,100):
        if int(str(j)[1])!=0 and int(str(j)[1])!=int(str(j)[0]):
            if float(i)/j==int(str(i)[0])/int(str(j)[1]) and int(str(i)[1])==int(str(j)[0]) : 
                if [i,j] not in result :
                    result.append([i,j])
        if int(str(j)[0])!=0 and int(str(j)[0])!=int(str(j)[1]):
            if float(i)/j==int(str(i)[1])/int(str(j)[0]) and int(str(i)[0])==int(str(j)[1]):
                if [i,j] not in result :
                    result.append([i,j])
                
a=np.prod([i for [i,j] in result])
b=np.prod([j for [i,j] in result])

p=pgcd(a,b)
print(b/p)
