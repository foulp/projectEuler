# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:58:21 2016

@author: timothee.boulet
"""

import numpy as np
from collections import Counter

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True
    
def SplitPrimeNumbers(n) :
    if isPrime(n) :
        return {n : 1}
    result=Counter({})
    temp=n
    for i in range(2,int(n**0.5)+1) :
        if temp%i==0 :
            dico1=Counter(SplitPrimeNumbers(i))
            dico2=Counter(SplitPrimeNumbers(n/i))
            result = result+dico1+dico2
            break            
    return result
            

def numberOfDivisors(n) :
    split = SplitPrimeNumbers(n).values()
    return np.prod([power+1 for power in split])

def FirstTriangle(overDivisors) :
    current = 1
    compteur = 2
    found=False
    while found==False :
        if numberOfDivisors(current)>overDivisors :
            found=True
        else :
            current = current+compteur
            compteur = compteur+1
    return current  
    
print(FirstTriangle(500))
