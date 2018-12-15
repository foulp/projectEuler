# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:03:43 2016

@author: Timothée Boulet
"""

compte=0
for i in range(10**4):
    temp=i
    Lyrchel=True
    for j in range(50):
        temp=temp+int(str(temp)[::-1])
        if str(temp)==str(temp)[::-1]:
            Lyrchel=False
            break
    if Lyrchel==True:
        compte+=1

print(compte)

"""
Answer : 249
"""