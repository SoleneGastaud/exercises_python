# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:16:21 2023

@author: s_gastaud21
"""

for k in range (1,11):
    if k %2 == 0:
        print(k)
    else:
        print(k**2)


quad_zahl = []

for k in range (1,11):
    if k %2 == 0:
        quad_zahl.append(k)
    else:
        quad_zahl.append(k**2)
        
print(quad_zahl)



    