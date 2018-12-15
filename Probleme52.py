# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:29:27 2016

@author: Timothée Boulet
"""
x=1
while True:
    if x%10000==0:
        print(x)
    temp=set(str(x))
    if set(str(2*x))==temp:
        if set(str(3*x))==temp:
            if set(str(4*x))==temp:
                if set(str(5*x))==temp:
                    if set(str(6*x))==temp:
                        break
    x+=1
    
print(x)

"""
Answer: 142857
"""