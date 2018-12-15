# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 16:23:52 2016

@author: timothee.boulet
"""

def square_root(n, limit):    
    string, digit = str(n).split('.'), []
    
    if len(string)>1:
        if len(string[0])%2==1:
            string[0]='0'+string[0]
        if len(string[1])%2==1:
            string[1]=string[1]+'0'
            
        while string[0]!='':
            digit.append(string[0][:2])
            string[0]=string[0][2:]
        while string[1]!='':
            digit.append(string[1][:2])
            string[1]=string[1][2:]
    
    else:
        if len(string[0])%2==1:
            string[0]='0'+string[0]
        while string[0]!='':
            digit.append(string[0][:2])
            string[0]=string[0][2:]
    
    digit=digit+['00']*(limit-len(digit))
    c=digit[0]
    digit.remove(c)
    c=int(c)
    p, x, test = 0, 0, 1
    while test<=c:
        x+=1
        test=(x+1)*(20*p+x+1)
    y=x*(20*p+x)
    result=[x]
    p=10*p+x
    r=c-y
    while (len(digit)>0 or r!=0) and len(result)<=limit:
        if len(digit)==0:
            c=='00'
        else:
            c=digit[0]
            digit.remove(c)
        c=100*r+int(c)
        x, test = 0, 20*p+1
        while test<=c:
            x+=1
            test=(x+1)*(20*p+x+1)
        y=x*(20*p+x)
        result.append(x)
        p=10*p+x
        r=c-y
    
    return result

total = 0
for n in range(2,100):
    if n not in [0,1,4,9,16,25,36,49,64,81,100]:
        test=square_root(n,100)
        total+=sum(test[:-1])
print(total)
        
        
    
        