# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:04:24 2016

@author: Timothée Boulet
"""
#from math import sin
limit=50
compte=0
for x1 in range(limit+1):
    for y1 in range(limit+1):
        for x2 in range(limit+1):
            for y2 in range(limit+1):
                a=x2**2+y2**2
                b=x1**2+y1**2
                c=(x1-x2)**2+(y1-y2)**2
                if all(z!=0 for z in [a,b,c]): #on vérifie que les points ne osient pas confondus
                    if  a+b==c:
                        compte+=1
                    elif a+c==b:
                        compte+=1
                    elif b+c==a:
                        compte+=1

#On a compté 2 fois chaque triangle possible
print(int(compte/2))

