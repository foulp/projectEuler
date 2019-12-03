# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:05:23 2016

@author: timothee.boulet
"""

def nextCollatz(n):
    if n%2==0 :
        return n/2
    else :
        return 3*n+1
    
def CollatzSequence(n) :
    if n==1:
        return [1]
    result = [n]
    suivant = n
    while suivant!=1:
        suivant = nextCollatz(suivant)
        result.append(suivant)
    return result

def longest_Collatz(n) :
    best = 0
    i_max = 0
    for i in range(1,n) :
        longueur = len(CollatzSequence(i))
        if best<longueur:
            best = longueur
            i_max = i
    return i_max, best
    
print(longest_Collatz(1000000))
