# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 21:42:48 2017

@author: SansAccent
"""

from itertools import combinations

def check_set(liste, n=7):        
    if any(sum(liste[:size])<=sum(liste[-size+1:]) for size in xrange(2,(n+1)/2+1)):
        return False
            
    for size in xrange(2,n/2+1):
        comb = []
        for c in list(combinations(liste,size)):
            somme = sum(c)
            if somme in comb:
                return False
            else:
                comb.append(somme)
    return True
    
with open("Probleme105_sets.txt", 'rb') as f:
    sets = f.read().split('\n')

sets = [[int(n) for n in s.split(',')] for s in sets]

total = 0
for s in sets:
    s.sort()
    if check_set(s, len(s)):
        total+=sum(s)
        
print total
