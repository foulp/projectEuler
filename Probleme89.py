# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 16:10:22 2016

@author: timothee.boulet
"""

"""
All the Roman numerals in the file contain no more than four consecutive identical units

Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.
"""

def isMinimal(roman):
    if 'XXXX' in roman or 'IIII' in roman or 'CCCC' in roman:
        return False
    return True
    
def minimal(roman):
    """
    Remplacer XXXX (40) par XL
    Remplacer IIII (4) par IV
    Remplacer CCCC (400) par CD
    
    Remplacer VIV (9) par IX
    Remplacer LXL (90) par XC
    Remplacer DCD (900) par CM
    """
    minimal=roman.replace('XXXX','XL').replace('IIII','IV').replace('CCCC','CD').replace('VIV','IX').replace('LXL','XC').replace('DCD','CM')
    return minimal



f=open('C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme89_roman.txt')
romans=f.read().split('\n')
f.close()

total=0
for roman in romans:
    if not isMinimal(roman):
        print roman
        total+=len(roman)-len(minimal(roman))

print(total)