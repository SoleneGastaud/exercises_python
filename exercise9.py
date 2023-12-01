# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:18:52 2023

@author: s_gastaud21
"""
import numpy as np

M = np.eye(5, dtype = "int")
M[3:, 0:2] = 2
M[0:2, 3:]= 3
print(M)