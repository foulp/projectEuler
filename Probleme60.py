# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:47:09 2016

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
    
start=[3,7,109,673]

i=677
while True:
    if i%10000==1:print(i)
    if all(isPrime(int(str(i)+str(j))) for j in start):
        if all(isPrime(int(str(k)+str(i))) for k in start):
            break
    i+=2
print(i)


i=677
while True:
    if i%10000==1:print(i)
    if all(isPrime(int(str(i)+str(j))) for j in start[:-1]):
        if all(isPrime(int(str(k)+str(i))) for k in start[:-1]):
            break
    i+=2
print(i) #6919


start2=[3,7,109,6919]
i=6921
while True:
    if i%10000==1:print(i)
    if all(isPrime(int(str(i)+str(j))) for j in start2):
        if all(isPrime(int(str(k)+str(i))) for k in start2):
            break
    i+=2
print(i) #29059


first=[3,7,109,6919,29059]
maxi=sum(first)

test=[3,7,109]
for j in range(6921, int((6919+29059)/2),2):
    if isPrime(j):
        test=[3,7,109,j]
        i=j+2
        while sum(test)+i<sum(first):
            if isPrime(i) and all(isPrime(int(str(i)+str(k))) for k in test) and all(isPrime(int(str(k)+str(i))) for k in test):
                print(i)                
                break
            i+=2

for i in range(3, int(maxi/5),2):
    if isPrime(i):
        test=[i]
        for j in range(i+2,int((maxi-i)/4),2):
            if isPrime(j) and isPrime(int(str(i)+str(j))) and isPrime(int(str(j)+str(i))):
                test=[i,j]
                for k in range(j+2,int((maxi-i-j)/3),2):
                    if isPrime(k) and all(isPrime(int(str(k)+str(h))) for h in test) and all(isPrime(int(str(h)+str(k))) for h in test):
                        test=[i,j,k]
                        for l in range(k+2,int((maxi-i-j-k)/2),2):
                            if isPrime(l) and all(isPrime(int(str(l)+str(h))) for h in test) and all(isPrime(int(str(h)+str(l))) for h in test):
                                test=[i,j,k,l]
                                for m in range(l+2,int(maxi-i-j-k-l),2):
                                    if isPrime(m) and all(isPrime(int(str(m)+str(h))) for h in test) and all(isPrime(int(str(h)+str(m))) for h in test):
                                        test=[i,j,k,l,m]
                                        if i+j+k+l+m<maxi:
                                            maxi=i+j+k+l+m
                                            best=test
            
            
            
            
            
            
            
        
