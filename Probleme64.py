# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:48:24 2016

@author: timothee.boulet
"""

def next_expansion(number, a, rest_a, rest_b):
    x=int(rest_b*(number**0.5+rest_a)/(number-rest_a**2))
    z=(number-rest_a**2)/rest_b
    y=z*x-rest_a
    return x,y,z
    

def sequence(n):
    a=int(n**0.5)
    rest_a=a
    rest_b=1
    sequence=[[a, rest_a, rest_b]]
    while True:
        a, rest_a, rest_b=next_expansion(n, a, rest_a, rest_b)
        if [a, rest_a, rest_b] in sequence:
            temp=sequence.index([a, rest_a, rest_b])
            break
        sequence.append([a, rest_a, rest_b])
    return [[x for x,y,z in sequence[:temp]], [x for x,y,z in sequence[temp:]]]
    
compteur=0
for i in range(10000):
    if i!=int(i**0.5)**2:
        temp=sequence(i)
        if len(temp[1])%2==1:
            compteur+=1
print(compteur)