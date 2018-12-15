# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:29:45 2017

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

best = 255
for a in xrange(19, (best-1)/7-2):
    for b in xrange(a+1, (best-1-a)/6-2):
        for c in xrange(b+1, (best-1-a-b)/5-1):
            for d in xrange(c+1, (best-1-a-b-c)/4-1):
                for e in xrange(d+1, (best-1-a-b-c-d)/3):
                    for f in xrange(e+1, (best-1-a-b-c-d-e)/2):
                        for g in xrange(f+1, (best-1-a-b-c-d-e-f)+1):
                            if check_set([a,b,c,d,e,f,g], n=7):
                                print [a,b,c,d,e,f,g]


#print check_set([20,31,38,39,40,42,45],7)
#print check_set([11,18,19,20,22,25],6)

