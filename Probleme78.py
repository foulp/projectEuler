# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 15:43:21 2016

@author: timothee.boulet
"""

def pentagonal(k):
    return k*(3*k-1)/2
    

n=0   
a=1
partitions=[a]
while a%(10**6) != 0:
    n+=1
    a=0
    k=1
    penta=pentagonal(k)
    while penta<=n:
        a+=(-1)**(k-1)*partitions[n-penta]
        if k<0:
            k=-k+1
        else:
            k=-k
        penta=pentagonal(k)
    a=int(a)
    partitions.append(a%10**6) #float error if not append %10**6


print(n)
        