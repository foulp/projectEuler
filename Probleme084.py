# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 15:23:07 2016

@author: timothee.boulet
"""
from collections import Counter
import random

seq=[0]
CC=[2,17,33]
CH=[7,22,36]
G2J=[30]

rolls=10**6
diceSize=4
compteur=0

for i in range(rolls):
    dice1=random.randint(1,diceSize)
    dice2=random.randint(1,diceSize)

    if dice1==dice2:
        compteur+=1
    else:
        compteur=0
    
    if compteur==3:
        compteur=0
        square=10
        
    else:    
        square=(dice1+dice2+seq[-1])%40
        
        if square in CC:
            odds=random.random()
            if odds<1/16.:
                square=0
            elif odds<2/16.:            
                square=10
                    
        if square in CH:
            odds=random.random()
            if odds<1/16.:
                square=0
            elif odds<2/16.:
                square=10
            elif odds<3/16.:
                square=11
            elif odds<4/16.:
                square=24
            elif odds<5/16.:
                square=39
            elif odds<6/16.:
                square=5
            elif odds<7/16.:
                if square in [7,36]:
                    square=12
                elif square==22:
                    square=28
            elif odds<9/16.:
                if square==7:
                    square=12
                elif square==22:
                    square=25
                elif square==36:
                    square=5
            elif odds<10/16.:
                square=(square-3)%40
          
        if square in G2J:
            square=10              
           
           
    seq.append(square)
   

   
total=Counter(seq)
maxi=[[0,-1],[0,-1],[0,-1]]
for key,value in total.iteritems():
    value=round(100*float(value)/rolls,2)
    if value>maxi[0][0]:
        maxi[0]=[value,key]
    maxi.sort()

for stop in maxi:
    string=str(stop[1])
    if len(string)==1:
        string='0'+string
    stop[1]=string
    
print(int(''.join([ma[1] for ma in maxi[::-1]])))
