# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:29:52 2016

@author: timothee.boulet
"""

def total_rectangles(m,n):
    return m*n*(m+1)*(n+1)/4



limit=2000000
best_epsi=limit
for m in range(1,2001):
    n=1
    total=total_rectangles(m,n)
    epsilon=abs(limit-total)
    
    while total<limit+best_epsi:
        if epsilon<best_epsi:
            best=[m,n]
            best_epsi=abs(limit-total)
        n+=1
        total=total_rectangles(m,n)
        epsilon=abs(limit-total)
    

print(best[0]*best[1], best, best_epsi)
    