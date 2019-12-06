# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:11:30 2016

@author: timothee.boulet
"""

def toBinary(n):
    return int(bin(n)[2:])
    
def isPalindrome(n):
    return n==int(str(n)[::-1])

def doubleBasedPalindrome(n):
    return isPalindrome(n) and isPalindrome(toBinary(n))

somme=0  
for i in range(1000001):
    if doubleBasedPalindrome(i):
        somme+=i
print(somme)
