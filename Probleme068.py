# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 13:13:31 2016

@author: timothee.boulet
"""
from itertools import permutations

numbers=list(range(1,11))

maxi=0
for permu in permutations(numbers,5):
    if 10 in permu:
        a,b,c,d,e = permu[0], permu[1], permu[2],permu[3], permu[4]
        if max([n for n in [a,b,c,d,e] if n<10])>=int(str(maxi)[0]):
            left = [j for j in range(1,11) if j not in [a,b,c,d,e]]
            for perm in permutations(left):
                f, g, h, i, j=  perm[0], perm[1], perm[2],perm[3], perm[4]
                test=a+f+g
                if test==b+g+h and test ==c+h+i and test==d+i+j and test==e+j+f:
                    temp=min(a,b,c,d,e)
                    if temp==a:
                        tr=int(''.join([str(n) for n in [a,f,g,b,g,h,c,h,i,d,i,j,e,j,f]]))
                    if temp==b:
                        tr=int(''.join([str(n) for n in [b,g,h,c,h,i,d,i,j,e,j,f,a,f,g]]))
                    if temp==c:
                        tr=int(''.join([str(n) for n in [c,h,i,d,i,j,e,j,f,a,f,g,b,g,h]]))
                    if temp==d:
                        tr=int(''.join([str(n) for n in [d,i,j,e,j,f,a,f,g,b,g,h,c,h,i]]))
                    if temp==e:
                        tr=int(''.join([str(n) for n in [e,j,f,a,f,g,b,g,h,c,h,i,d,i,j]]))
                    
                    maxi=max(tr,maxi)
                    
print(maxi)
