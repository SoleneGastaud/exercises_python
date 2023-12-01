# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:31:45 2023

@author: s_gastaud21
"""

import numpy as np
from numpy.linalg import inv

M = np.array([[3,1],[2,4]])
Minv = inv(M)

#print(Minv)

M2 = np.matmul(Minv, M)
print(M2)
