# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 14:06:03 2017

@author: SansAccent
"""
with open("Probleme102_triangles.txt") as fichier :
    triangles = fichier.read().split('\n')[:-1]


def containsOrigin(a,b,c):
    ##Case : 2 points are aligned with origin
    if a[0]*b[1]==a[1]*b[0] or c[0]*b[1]==c[1]*b[0] or a[0]*c[1]==a[1]*c[0]:
        return False
    ##Case :1 point is the origin
    if a[0]==a[1]==0 or b[0]==b[1]==0 or c[0]==c[1]==0:
        return False
        
    if a[0]!=0:
        w2 = (a[1]*c[0]-c[1]*a[0])/float(a[0]*b[1]-a[1]*b[0])
        w1 = -(w2*b[0]+c[0])/float(a[0])

        if w2>0 and w1>0:
            return True
        else:
            return False
    
    if a[0]==0 and b[0]!=0:
        w2 = - c[0]/float(b[0])
        w1 = -(c[1]+w2*b[1])/float(a[1])
        if w2>1 and w1>0:
            return True
        else:
            return False
    
somme = 0
for triangle in triangles:
    coord = triangle.split(',')
    a = [int(coord[0]),int(coord[1])]
    b = [int(coord[2]),int(coord[3])]
    c = [int(coord[4]),int(coord[5])]
    somme += containsOrigin(a,b,c)
        
    
            
