# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 11:12:44 2016

@author: timothee.boulet
"""

def sumProperDivisors(n):
    somme=1
    if int(n**0.5)**2==n:
        somme+=int(n**0.5)
    for k in range(2,int(n**0.5)):
        if n%k==0:
            somme += k + (n//k)
    return somme



limit=10**6

somme=[0]*2+[1]*(limit-1)

for n in range(2,limit):
    k=2
    while n*k<=limit:
        somme[n*k]+=n
        k+=1
        
longueur_chain={0:1}
longueur_extra={1:2, 2:3, 3:3, 4:4}
temp_chain, temp_extra = [], []
for n in range(5,limit+1):
    test=n
    previous, k = [], 0
    temp=temp_chain+temp_extra
    while test not in temp and test not in previous and test<=limit:
        previous.append(test)
        k+=1
        if test<=limit:
            test=somme[test]
        else:
            test=sumProperDivisors(test)
            
    if test in previous:
        stop=previous.index(test)
        for i,value in enumerate(previous):
            if i<stop:
                if len(temp_extra)<1000:
                    temp_extra.append(value)
                longueur_extra[value]=k-i
            else:
                temp_chain.append(value)
                longueur_chain[value]=k-stop
                
    elif test in temp_chain:
        for i,value in enumerate(previous):
            if len(temp_extra)<1000:
                temp_extra.append(value)
            longueur_extra[value]=k+longueur_chain[test]-i
    
    elif test in temp_extra:
        for i,value in enumerate(previous):
            if len(temp_extra)<1000:
                temp_extra.append(value)
            longueur_extra[value]=k+longueur_extra[test]-i
    
    elif test>limit:
        for i,value in enumerate(previous):
            if len(temp_extra)<1000:
                temp_extra.append(value)
            longueur_extra[value]=-1
            

maxi, keys = 0, []
for key,value in longueur_chain.iteritems():
    if value>maxi:
        keys=[key]
        maxi=value
    elif value==maxi:
        keys.append(key)
print(min(keys))
