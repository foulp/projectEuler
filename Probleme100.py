# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 14:18:49 2016

@author: timothee.boulet
"""

from fractions import gcd

limit=10**12
m=int(10**6/2**0.5)
found=False
while True:
    for temp in [(2*m**2+1)**0.5, (2*m**2-1)**0.5]:
        if int(temp)==temp:
            n=temp-m
            if gcd(m,n)==1:
                a=m**2-n**2
                b=2*m*n
                if abs(a-b)==1 and max(a,b)>=limit:
                    print('n vaut', max(a,b), 'et le nombre de bleus est', (1+(max(a,b)**2+(max(a,b)-1)**2)**0.5)/2)
                    found=True
    if found==True:
        break
    m+=1