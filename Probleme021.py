# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:15:59 2016

@author: timothee.boulet
"""
import numpy as np

def sumProperDivisors(n):
    if n==1 or n==0:
        return 0
    result=[1]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            if i!=n/i :
                result.append(n/i)
    return sum(result)


def amicable_numbers(n):
    result=[]
    for i in range(2,n):
        temp = sumProperDivisors(i)
        if temp!=i and [temp,i] not in result and sumProperDivisors(temp)==i:
            result.append([i, temp])
    return result


print(np.sum(amicable_numbers(10000)))
