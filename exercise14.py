# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:05:50 2023

@author: s_gastaud21
"""

import numpy as np

y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

Yd = ((y-np.mean(y))**2)
#print(Yd)

Yo = (1/10)*np.sum(Yd)
#print(Yo)

Yv = Yo**(1/2)
print(Yv)

Ysol = np.std(y)
print(Ysol)