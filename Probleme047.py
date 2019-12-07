# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:13:24 2016

@author: timothee.boulet
"""
Limit=10**6
factors=[0]*Limit
for i in xrange(2,Limit):
    if factors[i]==0: #isPrime
        k=2
        while k*i<Limit:
            factors[k*i]+=1
            k+=1
    elif factors[i]>=4:
        if all(value>=4 for value in factors[i+1:i+4]):
            print(i)
            break
        
        
#def isPrime(n) :
#    if n in [2,3,5,7] :
#        return True
#    if n==1 or n%10 in [0,2,4,5,6,8] :
#        return False
#    for i in range(3, int(n**0.5)+1,2) :
#        if n%i==0 : 
#            return False
#    return True
#    
#def primeDecomposition(n) :
#    result=[]
#    current=n
#    if n%2==0:
#        i=0
#        current=float(n)/2
#        while int(current)==current:
#            i+=1
#            current=float(current)/2
#        current=current*2
#        result.append([2,i])
#            
#    for i in range(3,int(n/2)+1,2):
#        if current==1:
#            break
#        if isPrime(i) and current%i==0:
#            j=0
#            current=float(current)/i
#            while int(current)==current:
#                j+=1
#                current=float(current)/i
#            current=current*i
#            result.append([i,j])
#            
#    return result
#    
#def firstFourPrimeConsecutiveDecomposition():
#    current=170000
#    temp1, temp2, temp3 = False, False, False
#    while True:
#        if current%1000 in [0,1,2,3]:
#            print(current)
#        if len(primeDecomposition(current))==4:
#            if temp3==False:
#                if len(primeDecomposition(current-1))<4:
#                    temp1, temp2, temp3 = True, False, False
#                    current+=3
#                else:
#                    if temp2==False:
#                        if len(primeDecomposition(current-2))<4:
#                            temp1, temp2, temp3 = True, True, False
#                            current+=2
#                        else:
#                            if temp1==False:
#                                if len(primeDecomposition(current-3))<4:
#                                    temp1, temp2, temp3 = True, True, True
#                                    current+=1
#                                else:
#                                    return current-3
#                            else:
#                                return current-3
#                    else:
#                        if temp1==False:
#                            if len(primeDecomposition(current-1))<4:
#                                temp1, temp2, temp3 = True, True, True
#                                current+=1
#                            else:
#                                return current-3
#                        else:
#                            return current-3
#            else:
#                if temp2==False:
#                    if len(primeDecomposition(current-2))<4:
#                        temp1, temp2, temp3 = True, True, False
#                        current+=2
#                    else:
#                        if temp1==False:
#                            if len(primeDecomposition(current-3))<4:
#                                temp1, temp2, temp3 = True, True, True
#                                current+=1
#                            else:
#                                return current-3
#                        else:
#                            return current-3
#                else:
#                    if temp1==False:
#                        if len(primeDecomposition(current-3))<4:
#                            temp1, temp2, temp3 = True, True, True
#                            current+=1
#                        else:
#                            return current-3
#                    else:
#                        return current-3                        
#        else:
#            temp1, temp2, temp3 = False, False, False
#            current+=4
#            
#
#p=4
#n=136930
#result=firstFourPrimeConsecutiveDecomposition()


#n=2*3*5*7
#found=False
#while found==False:
#    if any(len(primeDecomposition(i))<p for i in range(n,n+p)):
#        n+=1
#    else:
#        found=True
#print(n)
    
