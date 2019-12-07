# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:34:32 2016

@author: timothee.boulet
"""
import itertools

def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True
    

def primeDigitRemplacement(temp, size, compte):
    combi=itertools.combinations(range(len(temp)-1), size)
    for comb in combi:
        tot=[]
        test=[chiffre for chiffre in temp]
        compteur=0
        m=sum([int(chiffre) for chiffre in test])-int(test[comb[0]])-int(test[comb[1]])%3
        if m!=0:
            for i in range(10):
                if i!=0 or comb[0]!=0:
                    for index in comb:
                        test[index] = str(i)
                    number=int(''.join(test))
                    if isPrime(number):
                        tot.append(number)
                        compteur+=1
        if compteur==compte:
            print(comb)
            return True, min(tot)
    return False,0
    #120383

n=1001
while True:
    if isPrime(n):
        temp=str(n)
        for size in range(2,len(temp)):
            test=primeDigitRemplacement(temp,size,8)
            if test[0]==True:
                print(n, size)
                break
        if test[0] == True:
            break
    n+=2
    
print('Answer is :', test[1])
