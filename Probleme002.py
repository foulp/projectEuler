# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:29:53 2016

@author: Timothée Boulet
"""

def fibonnaci(n) :
    """
    Retourne tous les éléments de Fibonnaci jusqu'à n inclus
    """
    result = [1,2]
    while result[-1]+result[-2]<=n :
        result.append(result[-1]+result[-2])
    return result

liste = fibonnaci(4000000)
even = [liste[i] for i in range(len(liste)) if liste[i]%2==0]

print(sum(even))
    
    
