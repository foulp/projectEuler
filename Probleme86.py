# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 17:46:31 2016

@author: timothee.boulet
"""
#from fractions import gcd

def length_min(a,b,c):
    return (a**2+(b+c)**2)**0.5

#Tous les triplets pythagoriciens (a',b',c') où a'=a et b'=b+c  
limit=10**6
compte=0
a=1
while True:
    for bc in range(2,2*a+1):
            s = bc**2 + a**2
            if s==int(s**0.5)**2:
                if bc>a+1:
                    compte+=a+1 - (bc+1)//2
                else:
                    compte+=bc//2
    if compte>=limit:
        break
    if a==1818:
        print(compte)
    a+=1

print(a)
