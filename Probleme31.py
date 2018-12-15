# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:50:17 2016

@author: timothee.boulet
"""

def numberOfWays(value, coins):
    ways=[0]*(value+1)
    ways[0]=1
    for coin in coins:
        for i in range(coin,value+1):
            ways[i]+=ways[i-coin]
    return ways[value]

print(numberOfWays(200, [1,2,5,10,20,50,100,200]))

print(numberOfWays(100, list(range(1,101))))
