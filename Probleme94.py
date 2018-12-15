# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 16:48:38 2016

@author: timothee.boulet
"""
from fractions import gcd
from time import time

"""
Triplets pythagoriciens (a,b,c) tel que a**2+b**2=c**2, avec (c+/-1)/2=a ou (c+/-1)/2=b
Aire=(a**2-((a+/-1)/2)**2)**0.5*(a+/-1)/2
Perimeter=3*a +/- 1

Génération des triplets : a=2*m*n, b=m**2-n**2, c=m**2+n**2 où (m,n) co-prime et (m-n) impair positif
"""

t=time()
limit=10**9
total=0
m=2
while 3*(m**2+(m%2+1)**2)-1<=limit:
    
    n1=((m**2+1)/3.)**0.5
    if int(n1)==n1:
        if gcd(n1,m)==1 and 3*(m**2+n1**2)-1<=limit:
            a=m**2+n1**2
            b=(a-1)/2.
            area=b*(a**2-b**2)**0.5
            perimeter=3*a-1
            total+=perimeter
            print('1', m, n1, a, b, perimeter, area)
            
    n2=((m**2-1)/3.)**0.5
    if int(n2)==n2:
        if gcd(n2,m)==1 and 3*(m**2+n1**2)+1<=limit:
            a=m**2+n2**2
            b=(a+1)/2.
            area=b*(a**2-b**2)**0.5
            perimeter=3*(m**2+n2**2)+1
            total+=perimeter
            print('1', m, n2, a, b, perimeter, area)
    
    temp1=(3*m**2-1)**0.5
    if int(temp1)==temp1:            
        n1=2*m-temp1 #n<m !
        if gcd(n1,m)==1 and 3*(m**2+n1**2)+1<=limit:
            a=m**2+n1**2
            b=(a+1)/2.
            area=b*(a**2-b**2)**0.5
            perimeter=3*(n1**2+m**2)+1 
            total+=perimeter
            print('2', m, n1, a, b, perimeter, area)     
        
    
    temp2=(3*m**2+1)**0.5
    if int(temp2)==temp2:            
        n2=2*m-temp2 #n<m !
        if gcd(n2,m)==1 and 3*(m**2+n2**2)-1<=limit:
            a=m**2+n2**2
            b=(a-1)/2.
            area=b*(a**2-b**2)**0.5
            perimeter=3*(n2**2+m**2)-1 
            total+=perimeter
            print('2', m, n2, a, b, perimeter, area)
    m+=1

print int(total), 'calculé en', round((time()-t)*1000,0), 'ms'

