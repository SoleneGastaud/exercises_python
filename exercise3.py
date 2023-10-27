# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:36:20 2023

@author: s_gastaud21
"""

def steigung_funktion(z):
    x1 = z[0]
    y1 = z[1]
    x2 = z[2]
    y2 = z[3]
    
    steigung_funktion = (x2-x1)/(y2-y1)
    
    if x2 - x1 == 0:
        print("Die Steigung ist nicht definiert")
        
z = [4, 4, 8, 4]

w = steigung_funktion(z)

print(w)
    

def steigung_funktion(z):
    x1 = z[0]
    y1 = z[1]
    x2 = z[2]
    y2 = z[3]
    delta_x= x2 - x1
    delta_y = y2 - y1
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else:
        steigung = delta_y / delta_x
        print (steigung)
        

    
    