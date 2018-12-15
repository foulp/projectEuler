# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:07:12 2017
 
@author: tboulet
"""
 
d = {k:k-1 for k in range(1,201)}
dico = {k:[list(range(1,k+1))] for k in range(1,201)}
 
for k in range(1,200):
   for i,liste in enumerate(dico[k]):
      for val in liste:
         if val+k<=200:
            temp = list(set(dico[k][i]+[k+val]))
            if temp not in dico[k+val]:
               if d[k+val]>d[k]+1:
                  dico[k+val] = [temp]
                  d[k+val] = d[k]+1
               elif d[k+val]==d[k]+1:
                  dico[k+val].append(temp)
              
         
print sum(d.values())