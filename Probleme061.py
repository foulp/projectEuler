# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:54:09 2016

@author: timothee.boulet
"""

triangles = [n*(n+1)/2 for n in range(45,141)]

squares = [n**2 for n in range(32,100)]

pentagonals = [n*(3*n-1)/2 for n in range(26,82)]

hexagonals = [n*(2*n-1) for n in range(23,71)]

heptagonals = [n*(5*n-3)/2 for n in range(21,64)]

octogonals = [n*(3*n-2) for n in range(19,59)]

import itertools
            
liste=[squares, pentagonals, hexagonals, heptagonals, octogonals]

for orders in itertools.permutations([0,1,2,3,4]):
    for triangle in triangles:
           temp=int(str(triangle)[-2:])
           for square in liste[orders[0]]:
               if temp==int(str(square)[:2]) and square!=triangle:
                   temp2=int(str(square)[-2:])
                   for penta in liste[orders[1]]:
                       if temp2==int(str(penta)[:2]) and penta not in [triangle, square]:
                           temp3=int(str(penta)[-2:])
                           for hexa in liste[orders[2]]:
                               if temp3==int(str(hexa)[:2]) and hexa not in [triangle, square, penta]:
                                   temp4=int(str(hexa)[-2:])
                                   for hepta in liste[orders[3]]:
                                       if temp4==int(str(hepta)[:2]) and hepta not in [triangle, square, penta, hexa]:
                                           temp5=int(str(hepta)[-2:])
                                           for octa in liste[orders[4]]:
                                               if temp5==int(str(octa)[:2]) and int(str(octa)[-2:])==int(str(triangle)[:2]) and octa not in [hepta, hexa, triangle, square, triangle]:
                                                   print(sum([triangle, square, penta, hexa, hepta, octa]))
                                                   
               
       
    
    
    
