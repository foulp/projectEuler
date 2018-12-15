# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:06:00 2016

@author: timothee.boulet
"""

f=open('C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme79_keylog.txt')
lines=list(set(f.read().split('\n')[:-1]))
f.close()

digit=[set([line[0] for line in lines]), set([line[1] for line in lines]), set([line[2] for line in lines])]

prev_after=[]
for i in range(10):
    prev, after=[],[]
    for line in lines:
        if str(i) in line:
            stop=line.index(str(i))
            for j in line[:stop]:
                if j not in prev:
                    prev.append(j)
            for j in line[stop+1:]:
                if j not in after:
                    after.append(j)
    prev_after.append([prev, after])

longueur=[]
for i, temp in enumerate(prev_after):
    length=len(temp[0])
    if length==0 and len(temp[1])==0:
        pass
    else:
        longueur.append([length,i])

longueur.sort()

print(int(''.join([str(i) for l,i in longueur])))

