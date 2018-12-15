# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:27:40 2017

@author: SansAccent
"""
import numpy as np

with open("Probleme107_network.txt","rb") as net:
    network = np.array([ligne.split(',') for ligne in net.read().split('\n')[:-1]])

edges, totalWeight = [], 0
for i in xrange(40):
    for j in xrange(i+1,40):
        edge = network[i,j]
        if edge=='-':
            pass
        else:
            totalWeight+=int(edge)
            edges.append([int(edge),i, j])
        
edges.sort()


#Kruskal Algorithm
total = 0
connexe = []
for edge in edges :
    w, i, j = edge
    if any(i in tree and j in tree for tree in connexe):
        pass
    elif any(i in tree or j in tree for tree in connexe)==False:
        connexe.append([i,j])
        total+=w
    else:
        total+=w
        places = {i:[], j:[]}
        for k, tree in enumerate(connexe):
            if i in tree:
                places[i]=k
            elif j in tree:
                places[j]=k
        if places[i]==[]:
            connexe[places[j]] = connexe[places[j]]+[i]
        elif places[j]==[]:            
            connexe[places[i]] = connexe[places[i]]+[j]
        else:
            connexe[places[i]] = connexe[places[i]]+connexe[places[j]]
            connexe.remove(connexe[places[j]])
    
    if len(connexe)==1 and connexe[0]==list(range(40)):
        break
        
print totalWeight-total
        