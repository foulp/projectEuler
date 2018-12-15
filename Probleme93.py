# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 16:59:50 2016

@author: timothee.boulet
"""
import itertools
import operator

maxi=0
ops = {0:operator.add, 
       1:operator.sub,
       2:operator.div,
       3:operator.mul}

for w in range(1,10):
    for x in range(w+1,10):
        for y in range(x+1,10):
            for z in range(y+1,10):
                total=[]
                for permu in itertools.permutations([float(w), float(x), float(y), float(z)]):
                    a,b,c,d = permu[0], permu[1], permu[2], permu[3]
                    
                    for oper in itertools.product(range(4),repeat=3):
                        o1,o2,o3 = oper[0], oper[1], oper[2]
                        
                        for order in itertools.permutations([o1,o2,o3]):
                            if order[0]==o1:
                                temp=ops[o1](a,b)
                                if order[1]==o2:
                                    temp=ops[o2](temp,c)
                                    temp=ops[o3](temp,d)
                                else:
                                    tempi=ops[o3](c,d)
                                    temp=ops[o2](temp, tempi)
                                    
                            elif order[0]==o2:
                                temp=ops[o2](b,c)
                                if order[1]==o1:
                                    temp=ops[o1](a,temp)
                                    temp=ops[o3](temp,d)
                                else:
                                    temp=ops[o3](temp,d)
                                    if temp==0 and o1==2:
                                        break
                                    temp=ops[o1](a,temp)
                            
                            elif order[0]==o3:
                                temp=ops[o3](c,d)
                                if order[1]==o1:
                                    tempi=ops[o1](a,b)
                                    temp=ops[o2](tempi,temp)
                                else:
                                    temp=ops[o2](b,temp)
                                    if temp==0 and o1==2:
                                        break
                                    temp=ops[o1](a,temp)
                            
                            if int(temp)==temp and temp>0:
                                total.append(temp)

                total=list(set(total))
                total.sort()
                i=1
                while i in total:
                    i+=1
                if i-1>maxi:
                    maxi=i-1
                    print(w,x,y,z)