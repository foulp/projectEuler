# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 16:39:07 2016

@author: timothee.boulet
"""
import numpy as np
import itertools

def areAnagrams(w1, w2):
    l1, l2 = len(w1), len(w2)
    if l1!=l2:
        return False
    
    t1=list(w1)
    t2=list(w2)
    
    for letter in t1:
        if letter not in t2:
            return False
        else:
            t2.remove(letter)
    return True

f=open('C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme98_words.txt', 'r')
words=[word[1:-1] for word in f.read().split(',')]
f.close()

square=[n**2 for n in range(1,1000)]

separe=[[]]*14
for i,word in enumerate(words):
    words[i]=[len(word), word]
    separe[len(word)-1]=separe[len(word)-1]+[word]
separe=separe[::-1]
words.sort()
words=[word[1] for word in words[::-1]]

pairs=[]
for liste in separe:
    for j,word in enumerate(liste):
        for wordi in liste[j+1:]:
            if areAnagrams(word, wordi) and len(np.unique(list(word)))<10:
                pairs.append([word,wordi])
                
final=[]
for pair in pairs:
    w1, w2 = pair[0], pair[1]
    size=np.unique(list(w1))
    for permu in itertools.permutations(list(range(10)),len(size)):
        replace = {size[i]:permu[i] for i in range(len(size))}
        number=int(''.join([str(replace[letter]) for letter in w1]))
        if int(number**0.5)**2==number and replace[w1[0]]!=0 and replace[w2[0]]!=0:
            other=int(''.join([str(replace[letter]) for letter in w2]))
            if int(other**0.5)**2==other:
                print pair, number, other, number**0.5, other**0.5
                final.append(max(number, other))
                
print(max(final))
