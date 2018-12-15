# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:40:41 2016

@author: timothee.boulet
"""
def squareDigits(n):
    return sum([int(numb)**2 for numb in str(n)])


previous1=[1]
previous89=[2,3,4]
previous={1:1,2:89,3:89,4:89,89:89}
size=154
for n in range(5,10**7):
    if len(previous.keys())<size:
        test=squareDigits(n)
        temp=False
        while test not in previous1 :
            if test in previous89:
                temp=True
                break
            test=squareDigits(test)
        if temp==False:
            previous1.append(n)
            previous[n]=1
        else:
            previous89.append(n)
            previous[n]=89
    else:
        test=squareDigits(n)
        while test not in previous.keys():
            test=squareDigits(test)
        if previous[test]==89:
            previous89.append(n)
        else:
            previous1.append(n)

print(len(set(previous89)))