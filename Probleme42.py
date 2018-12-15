# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:46:37 2016

@author: timothee.boulet
"""
import string
dico = dict(zip(string.ascii_uppercase, range(1,27)))

text_file = open('Probleme42_words.txt', "r")
lines = text_file.read().split(',')
text_file.close()


def isTriangleNumber(n):
    if n==0: 
        return False
    temp=float(-1+(1+8*n)**0.5)/2
    return temp==int(temp)


total=0
for word in lines:
    score=0
    temp=word[1:-1]
    for letter in temp:
        score+=dico[letter]
    if isTriangleNumber(score):
        total+=1

print(total)