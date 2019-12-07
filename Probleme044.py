# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:36:01 2016

@author: timothee.boulet
"""

def Pentagonal(n):
    return n*(3*n-1)/2

def isPentagonal(n):
    temp=float(1+(1+24*n)**0.5)/6
    return temp==int(temp)
    
#
#max_n=10000
#a=[Pentagonal(n) for n in range(1,max_n)]
#aa=[x-y for x in a for y in a if x-y in a and x+y in a]
#print(min(aa))

D=float('inf')
n_max=10000
#n=1
#while Pentagonal(n+1)-Pentagonal(n)<D:
for n in range(1,n_max):
    if n%100==0:
        print(n)
    Pk=Pentagonal(n)
    for i in range(1,n):
        Pj=Pentagonal(i)
        if isPentagonal(abs(Pk-Pj)) and isPentagonal(Pk+Pj):
            D=min(D, abs(Pk-Pj))
            print("New D is",D)
#    n+=1
    
print(D)
