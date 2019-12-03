# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:23:54 2016

@author: timothee.boulet
"""
unit = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
teen = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
dozen = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

def word(n):
    if n<10:
        return unit[n]
    if n<20:
        return teen[n]
    if n<100:
        if n%10!=0:
            return dozen[n//10]+''+unit[n%10]
        else :
            return dozen[n//10]
    else :
        if n%100!=0 :
            return unit[n//100]+'hundredand'+word(n%100)
        else :
            return unit[n//100]+'hundred'
    
def len_total(n):
    somme=0
    for i in range(1,n):
        somme = somme+len(word(i))
    return somme+len('onethousand')
        
print(len_total(1000))
