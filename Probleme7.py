# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:53:12 2016

@author: Timothée Boulet
"""

def NumberPrime(n):
    """Return the nth prime number"""
    test=3
    liste = [2]
    while len(liste)<n :
        if any(test%nombre==0 for nombre in liste)==False :
            liste.append(test)
        test=test+2
    return liste[-1]
    

print(NumberPrime(10001))