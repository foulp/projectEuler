# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:54:30 2016

@author: timothee.boulet
"""
import numpy as np

f=open("C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme83_matrix.txt",'r')
matrix=f.read().split('\n')[:-1]
f.close()

for i,line in enumerate(matrix) :
    matrix[i]=[int(numb) for numb in line.split(',')]

#matrix=[[131,673,234,103,18],
#        [201,96,342,965,150],
#        [630,803,745,422,111],
#        [537,699,497,121,956],
#        [805,732,524,37,331]]


#Initalisation
def init(matrix):
    m=len(matrix)
    values=np.ones((m,m))*10**6
    before=np.array((m,m))
    
    values[0,0]=matrix[0][0]
    return values, before

#Recherche d'un noeud de distance minimale
def trouver_min(Q, values):
    spike=[0,0]
    mini=10**7
    for sommet in Q:
        i,j=sommet[0], sommet[1]
        if values[i,j]<mini:
                mini=values[i,j]
                spike=[i,j]
    return spike

def maj_distances(s1,s2, values, before):
    test=values[s1[0],s1[1]] + matrix[s2[0]][s2[1]]
    if values[s2[0],s2[1]] > test:
        values[s2[0],s2[1]] = test
        #before[s2[0],s2[1]] = s1
    return True

def Dijkstra(matrix):
    m=len(matrix)
    values, before = init(matrix)
    Q=[[i,j] for i in range(m) for j in range(m)]
    while len(Q)>0:
        s1=trouver_min(Q, values)
        Q.remove(s1)
        i,j=s1[0],s1[1]
        if i==0 and j>0 and j<m-1:
            maj_distances(s1, [0,j-1], values, before)
            maj_distances(s1, [1,j], values, before)
            maj_distances(s1, [0,j+1], values, before)
        elif j==0 and i>0 and i<m-1:
            maj_distances(s1, [i-1,0], values, before)
            maj_distances(s1, [i,1], values, before)
            maj_distances(s1, [i+1,0], values, before)
        elif j==0 and i==m-1:
            maj_distances(s1, [i-1,0], values, before)
            maj_distances(s1, [i,1], values, before)
        elif i==0 and j==m-1:
            maj_distances(s1, [0,j-1], values, before)
            maj_distances(s1, [1,j], values, before)
        elif i==m-1 and j>0 and j<m-1:
            maj_distances(s1, [i,j-1], values, before)
            maj_distances(s1, [i-1,j], values, before)
            maj_distances(s1, [i,j+1], values, before)            
        elif j==m-1 and i>0 and i<m-1:
            maj_distances(s1, [i-1,j], values, before)
            maj_distances(s1, [i,j-1], values, before)
            maj_distances(s1, [i+1,j], values, before)  
        elif j==m-1 and i==m-1:
            maj_distances(s1, [i-1,j], values, before)
            maj_distances(s1, [i,j-1], values, before)
        elif i==0 and j==0:
            maj_distances(s1, [i+1,j], values, before)
            maj_distances(s1, [i,j+1], values, before)            
        else:
            maj_distances(s1, [i-1,j], values, before)
            maj_distances(s1, [i,j-1], values, before)             
            maj_distances(s1, [i+1,j], values, before)
            maj_distances(s1, [i,j+1], values, before) 
            
    return values


values = Dijkstra(matrix)
    
print(int(values[-1,-1]))
