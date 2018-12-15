# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:33:34 2016

@author: Timothée Boulet
"""

def isPalindrome(n):
    return str(n)==str(n)[::-1]

def maxPalindrome(n):
    maximum=0
    for i in range(10**(n-1),10**n) :
        for j in range(10**(n-1),10**n) :
            temp=i*j
            if temp>maximum :
                if isPalindrome(i*j) :
                    maximum=i*j
    return maximum

print(maxPalindrome(3))
        