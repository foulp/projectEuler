# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:22:03 2016

@author: timothee.boulet
"""
import string
dico = dict(zip(string.ascii_uppercase, range(1,27)))

text_file = open('Probleme022_names.txt', "r")
lines = text_file.read().split(',')
text_file.close()

lines.sort()

scores=0
for i,name in enumerate(lines):
    score = 0
    temp = name[1:-1]
    for letter in temp :
        score+=dico[letter]
    scores+=score*(i+1)

print(scores)


    


