# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:01:26 2023

@author: s_gastaud21
"""

import numpy as np


D= np.tile(np.arange(1, 11), 10)
D_C = D.reshape(10,10)

D_Z = D_C.sum(axis = 0)
D_S = D_C.mean(axis =1)


print(D_Z)
print(D_S)



