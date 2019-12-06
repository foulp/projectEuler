# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:20:53 2016

@author: timothee.boulet
"""

def fact(n):
    if n<2:
        return 1
    return fact(n-1)*n

final = []

found=False
k=1
while found==False:
    limit = 10**k-1
    if sum([fact(int(nb)) for nb in str(limit)])<limit:
        found=True
    else:
        k+=1

for i in range(10,10**k):
    if sum([fact(int(nb)) for nb in str(i)])==i:
        final.append(i)

print(sum(final))
