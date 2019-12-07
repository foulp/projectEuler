# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:49:05 2016

@author: timothee.boulet
"""
from collections import Counter
import operator

cardValues = [2,3,4,5,6,7,8,9,10,11,12,13,14]

handValues = {'High':0, 'Paire':1, 'Double paire':2, 'Brelan':3, 'Suite':4, 'Couleur':5, 'Full':6, 'Carre':7, 'Quinte Flush':8}

def handValue(cards, colors):
    color, suite, wheel = False, False, False
    if cards==[2,3,4,5,14]:
        wheel=True
        suite=True
    if len(set(colors))==1:
        color=True
    if sublistExists(cardValues, cards) :
        suite=True
    
    if color==True and suite==True:
        if wheel==True:
            return [handValues['Quinte Flush'], 5]
        else:
            return [handValues['Quinte Flush'], [max(cards)]]

    if color==True and suite==False:
            return [handValues['Couleur'], [max(cards)]]
    
    if color==False and suite==True:
        if wheel==False:
            return [handValues['Suite'], [max(cards)]]
        else:
            return [handValues['Suiter'], [5]]
    
    compte = Counter(cards)
    compte = sorted(compte.items(), key=operator.itemgetter(1))
    if len(compte)==5:
        temp=[key for key,value in compte[::-1]]
        temp.sort()
        return [handValues['High'], temp[::-1]]
    if len(compte)==4:
        temp=[key for key,value in compte[-2::-1]]
        temp.sort()
        temp.append(compte[-1][0])
        return [handValues['Paire'], temp[::-1] ]
        
    compteur=1
    for key, value in compte[::-1]:
        if value==4:
            return [handValues['Carre'], [key]]
        if value==3 and len(compte)==2:
            return [handValues['Full'], [key]]
        if value==3 and len(compte)==3:
            return [handValues['Brelan'], [key]]
        if value==2 and compteur==1:
            temp=key
        if value==2 and compteur==2:
            temp2=key
        if compteur==3:
            return [handValues['Double paire'],[max(temp,temp2), min(temp2,temp), key]]
            
        compteur+=1
        
    
        
        
def sublistExists(list1, list2):
    return ''.join(map(str, list2)) in ''.join(map(str, list1))

def handWinner(main):
    hand0 = [[hand[0], hand[1]] for hand in main[0].split(' ')]
    hand1 = [[hand[0], hand[1]] for hand in main[1].split(' ')]
    
    colors0 = [color for  card,color in hand0]
    cards0 = [card for  card,color in hand0]
    colors1 = [color for  card,color in hand1]
    cards1 = [card for  card,color in hand1]
    
    for i,card in enumerate(cards0):
        if card=='T':
            cards0[i]='10'
        if card=='J':
            cards0[i]='11'
        if card=='Q':
            cards0[i]='12'
        if card=='K':
            cards0[i]='13'
        if card=='A':
            cards0[i]='14'
    cards0=[int(card) for card in cards0]
    cards0.sort()
    
    for i,card in enumerate(cards1):
        if card=='T':
            cards1[i]='10'
        if card=='J':
            cards1[i]='11'
        if card=='Q':
            cards1[i]='12'
        if card=='K':
            cards1[i]='13'
        if card=='A':
            cards1[i]='14'
    cards1=[int(card) for card in cards1]
    cards1.sort()
    
    player0 = handValue(cards0, colors0)
    player1 = handValue(cards1, colors1)
    
    if player0[0]>player1[0]:
        return 0
    elif player0[0]<player1[0]:
        return 1
    else:
        i=0
        while True:
            if player0[1][i]>player1[1][i]:
                return 0
            elif player0[1][i]<player1[1][i]:
                return 1
            i+=1
    
    
f = open('Probleme054_mains.txt', "r")
hands=[]
for line in f:
    line=line[:-1]
    hands.append([line[:14], line[15:]])

compte=0
for hand in hands:
    test=handWinner(hand)
    if test==0:
        compte+=1

print(compte)
