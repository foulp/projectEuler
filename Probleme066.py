# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 16:48:59 2016

@author: timothee.boulet
"""

from fractions import gcd


def next_hk(a,h,k,n):
    hi,ki = a[(n-1)%len(a)]*h[-1]+h[-2], a[(n-1)%len(a)]*k[-1]+k[-2]
        
    g=gcd(hi,ki)
    return hi/g,ki/g
    

def CF(n):
    ai=int(n**0.5)
    xi = [ai , n-ai**2]
    x,a=[xi],[ai]
    while xi[0]!=a[0] or xi[1]!=1 :
        ai=int( (n**(0.5)+xi[0]) / xi[1])
        i,j=xi[0],xi[1]
        xi=[j, i-ai*j]
        i,j=xi[0],xi[1]
        xi=[-j, (n-j**2)/i]
        
        x.append(xi)        
        a.append(ai)
    
    a.append(2*a[0])
    return a 
        


limit=1000
maxi=0
d_best=0
for d in range(2,limit+1) :
    if int(d**0.5)**2!=d:
        a=CF(d)
        h, k = [0,1], [1,0]
        h0, k0 = a[0]*h[-1]+h[-2], a[0]*k[-1]+k[-2]
        h.append(h0)
        k.append(k0)
        a=a[1:]
        n=1
        while True:
            hn,kn=next_hk(a,h,k,n)
            if hn**2-d*kn**2==1:
                print d,':',hn,',',kn
                if hn>maxi:
                    d_best=d
                    maxi=hn
                break
            h.append(hn)
            k.append(kn)
            n+=1
            
print(d_best)
