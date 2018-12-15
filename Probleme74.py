# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:38:54 2016

@author: timothee.boulet
"""
import numpy as np

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)



#%%
limit=10**6
edge=500
prev={}
chain={}
for n in range(limit):
    if n<edge:
        previous=[n]
        test=sum([fact(int(numb)) for numb in str(n)])
        while test not in previous:
            previous.append(test)
            test=sum([fact(int(numb)) for numb in str(test)])
        
        stop=previous.index(test)
        taille=len(previous)
        for i, numb in enumerate(previous):
            if i<stop:
                chain[numb]=taille-i
            else:
                chain[numb]=taille-stop           
    else:
        temp=False
        if n==edge:
            prev=chain.copy()
        previous=[n]
        test=sum([fact(int(numb)) for numb in str(n)])
        while test not in prev.keys():
            if test in previous:
                temp=True
                break
            previous.append(test)
            test=sum([fact(int(numb)) for numb in str(test)])
        
        if temp==True:
            stop=previous.index(test)
            taille=len(previous)
            for i, numb in enumerate(previous):
                if i<stop:
                    chain[temp]=taille-i
                else:
                    chain[temp]=taille-stop
        else:
            taille=len(previous)
            for i, numb in enumerate(previous):
                chain[numb]=chain[test]+taille-i
        

print(len(np.where(np.array(chain.values())==60)[0]))        
    