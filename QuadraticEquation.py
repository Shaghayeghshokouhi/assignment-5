# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:27:57 2023

@author: 2022
"""
import math

def QuadraticEquation():
    a = float(input("enter a:"))
    b = float(input("enter b:"))
    c = float(input("enter c:"))
    delta = (b**2)-(4*a*c)
    
    if delta < 0:
        print("no result")
    elif delta == 0:
        x = (-b + math.sqrt(b**2)-(4*a*c)) / (2 * a)
        print(x)
    elif delta > 0:
        rishe1 = (-b + math.sqrt(b**2)-(4*a*c)) / (2 * a)
        rishe2 = (-b - math.sqrt(b**2)-(4*a*c)) / (2 * a)
        print(rishe1, rishe2)
        
QuadraticEquation()
      
        
    
    
                        
    