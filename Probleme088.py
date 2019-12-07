# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:36:48 2016

@author: timothee.boulet
"""
def isPrime(n) :
    if n in [2,3,5,7] :
        return True
    if n==1 or n%10 in [0,2,4,5,6,8] :
        return False
    for i in range(3, int(n**0.5)+1,2) :
        if n%i==0 : 
            return False
    return True
    

limit=12000
keys=[2]
result={2:4}
decompo=[[],[],[],[],[[2,2]]]
n=5
while sum(keys)<limit*(limit+1)/2-1:
    temp=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if isPrime(i)==False:
                un=decompo[i]
                for dec in un:
                    test=dec+[n//i]
                    test.sort()
                    if test not in temp:
                        temp.append(test)
            if isPrime(n//i)==False:
                deux=decompo[n//i]
                for dec in deux:
                    test=dec+[i]
                    test.sort()
                    if test not in temp:
                        temp.append(test)
            if [i,n//i] not in temp:
                temp.append([i,n//i])
            
    decompo.append(temp)
    
    for deco in temp:
        somme=sum(deco)
        diff=n-somme
        taille=diff+len(deco)
        if taille not in result.keys():
            result[taille]=n
            if taille<=limit:
                keys.append(taille)
    n+=1

print(sum(set([value for key,value in result.iteritems() if key<=limit])))
     
