# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:48:44 2023

@author: s_gastaud21
"""

import pandas as pd
import numpy as np

data = pd.read_csv("Hausaufgabe.py")

data_separate = data.sort_values(by = ["Date", "Adj Close"])

print(data_separate)