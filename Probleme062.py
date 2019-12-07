# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:47:30 2016

@author: timothee.boulet
"""
def areAnagrams(str1, str2):
    # Sort both strings
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
 
    # Compare sorted strings
    for i in xrange(len(str1)):
        if str1[i] != str2[i]:
            return 0 
    return 1


k=5
current=3
temp=[]
found=False
while True:
    test=k**3
    test_str=str(test)
    match=False
    if len(test_str)==current:
        for i,first in enumerate([numbers[0] for numbers in temp]):
            if areAnagrams(test_str, str(first))==1:
                match=True
                temp[i].append(test)
                break        
        if match==False:
            temp.append([test])
            
    else:
        for i in xrange(len(temp)):
            if len(temp[i])==5:
                found=True
                print(min(temp[i]))
                break
        if found==True:
            break
        
        current=len(test_str)    
        temp=[[test]]
    
    k+=1 
