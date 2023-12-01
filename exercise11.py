# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:29:45 2023

@author: s_gastaud21
"""

import numpy as np

E = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]], [[9,8,7], [3,2,1], [6,5,4]]])

print(E.sum(axis=0))