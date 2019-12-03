# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:17:15 2016

@author: timothee.boulet
"""
def isSunday(day):
    return day%7==0
     
def firstOfYears():
    seq = [1,366]
    for i in range(1,100):
        if i%4==0:
            seq.append(seq[-1]+366)
        else:
            seq.append(seq[-1]+365)
    return seq
     
def firstOfMonths(year, firstOfyears):
    if year==2000:
        seq=[firstOfyears[-1]]
    else:
        seq=[firstOfyears[int(str(year)[-2:])]]
    seq.append(seq[-1]+31)
    if year%4==0:
        seq.append(seq[-1]+29)
    else :
        seq.append(seq[-1]+28)
    for nbr in [31,30,31,30,31,31,30,31,30]:
        seq.append(seq[-1]+nbr)
    return seq

years = firstOfYears()
somme=0
for year in range(1901,2001):
    months = firstOfMonths(year, years)
    for day in months:
        if isSunday(day):
            somme+=1

print(somme)
        
    
    
    
