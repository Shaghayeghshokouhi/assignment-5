# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:44:29 2023

@author: 2022
"""

def shatranji():
    n = int(input("enter n:"))
    m = int(input("enter m:"))
    mat = []
    
    for i in range(n):
        a=[]
        b=[]
        
        for j in range (m):
            a.append("#")
            a.append("*")
            b.append("#")
            b.append("*")
        mat.append(a)
        mat.append(b)
        
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end ="")
            
shatranji()
      