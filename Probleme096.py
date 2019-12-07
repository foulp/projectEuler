# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:01:25 2016

@author: Timothée Boulet
"""
import numpy as np
import re
from itertools import product

def possibleValues(sudo, i, j):
    k, l = i%3, j%3    
    toRemove = list(set(range(1,10)) - set(list(sudo[i,:]) + list(sudo[:,j]) + 
                   list(sudo[i-k:i-k+3, j-l:j-l+3].reshape(9))))
    toRemove.sort()
    return toRemove
    
    
def solveSudo(sudo):
    from copy import deepcopy
    result = deepcopy(sudo)
    possibles = []
    for i in range(9):
        temp = [possibleValues(sudo,i,j) if sudo[i,j]==0 else [] for j in range(9)]
        possibles.append(temp)
    possibles = np.array(possibles)
    lastGood, lastGood1 = [], []
    guess, current, idx = [], [], []

    while 0 in result:
        photo = deepcopy(result)
        photo2 = deepcopy(possibles)
        result, possibles = nextValue(result, possibles)     
                    
        if all(photo[i,j]==result[i,j] and photo2[i,j]==possibles[i,j] for i,j in product(range(9), repeat=2)):
            lastGood.append(deepcopy(result)) 
            lastGood1.append(deepcopy(possibles))
            for i,j in product(range(9), repeat=2):
                if len(possibles[i,j])>=2 and (i,j) not in idx:
                    idx.append((i,j))
                    guess.append(possibles[i,j])
                    break
            current.append(0)
            result[idx[-1]] = guess[-1][0]
            possibles = removeValue(possibles, idx[-1], guess[-1][0])

        if correctSudo(result, possibles)==False:
            while current[-1]==len(guess[-1])-1:
                lastGood = lastGood[:-1]
                lastGood1 = lastGood1[:-1]
                current = current[:-1]
                guess = guess[:-1]
                idx = idx[:-1]
            
            result, possibles = lastGood[-1], lastGood1[-1]
            current[-1] += 1
            result[idx[-1]] = guess[-1][current[-1]]
            possibles = removeValue(possibles, idx[-1], guess[-1][current[-1]])

    return result
        
    
def nextValue(sudo, possibles):
    result = sudo.copy()
    result1 = possibles.copy()
    for idx, x in np.ndenumerate(possibles):
        if len(x)==1:
            result[idx] = x[0]
            result1 = removeValue(result1, idx, x[0])
    
    for digit in range(1,10):
        for k in range(9):
            ligne = [i for i in range(9) if  digit in result1[i,k]]
            column = [j for j in range(9) if digit in result1[k,j]]
            if len(ligne)==1:
                result[ligne[0],k]=digit
                result1 = removeValue(result1, (ligne[0],k), digit)
            if len(column)==1:
                result[k,column[0]]=digit
                result1 = removeValue(result1, (k,column[0]), digit)
        
        for i,j in product(range(0,9,3), repeat=2):
            square = [(i+k,j+l) for k,l in product(range(3), repeat=2) if digit in result1[i+k,j+l]]
            if len(square)==1:
                result[square[0][0], square[0][1]]=digit
                result1 = removeValue(result1, square[0], digit) 
        
    return result, result1
                
def correctSudo(sudo, possibles):
    from collections import Counter
    for k in range(9):
        temp = Counter([val for val in sudo[k,:] if val!=0])
        temp1 = Counter([val for val in sudo[:,k] if val!=0])
        if any(val>1 for val in temp.values()) or any(val>1 for val in temp1.values()):
            return False
        missing_ligne = set(range(1,10))-set(sudo[k,:])
        missing_column = set(range(1,10))-set(sudo[:,k])
        possibles_ligne, possibles_column = [], []
        for f in possibles[k,:]:possibles_ligne+=f
        for f in possibles[:,k]:possibles_column+=f
        if missing_ligne!=set(possibles_ligne) or missing_column!=set(possibles_column):
            return False
            
    for i,j in product(range(0,9,3), repeat=2):
        square = [sudo[i+k,j+l] for k,l in product(range(3), repeat=2)]
        temp = Counter([val for val in square if val!=0])
        if any(val>1 for val in temp.values()):
            return False
        
        missing = set(range(1,10)) - set(sudo[i:i+3,j:j+3].reshape(9))
        possible = []
        for f in possibles[i:i+3,j:j+3].reshape(9):possible+=f
        if missing!=set(possible):
            return False
            
    return True
                
    
def removeValue(possibles, idx, val):
    result = possibles.copy()
    i,j = idx
    result[i,j]=[]
    for k in range(9):
        if val in result[k,j]:
            result[k,j].remove(val)
        if val in result[i,k]:
            result[i,k].remove(val)
    for k,l in product(range(3), repeat=2):
        if val in result[3*(i//3)+k, 3*(j//3)+l]:            
            result[3*(i//3)+k, 3*(j//3)+l].remove(val)
    return result
     
        
with open('Probleme096_sudoku.txt') as file:
    sudos = file.read()
    sudos = re.sub(r'\n','', sudos)
    sudos = re.split(r'Grid [0-9]{2}', sudos)[1:]
    somme = 0
    for k,sudo in enumerate(sudos):
        sudo = np.array([int(digit) for digit in sudo]).reshape((9,9))
        sudos[k]=sudo
        sol = solveSudo(sudo)
        somme += int(''.join([str(val) for val in sol[0, :3]]))
        print k
