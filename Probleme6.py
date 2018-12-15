# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:47:59 2016

@author: Timothée Boulet
"""

liste = list(range(101))
liste2 = [chiffre**2 for chiffre in liste]

print(abs(sum(liste)**2-sum(liste2)))