# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:16:48 2023

@author: s_gastaud21
"""


satz = "Hallo, Berlin"

satz_list = list(satz)
count_letters = []

for buchstabe in satz_list:
    if buchstabe.isalpha() == 1:
        count_letters.append(buchstabe.isalpha())
     
print(sum(count_letters))

def buchstabe_zählen(x):
    x_list = list(x)
    x_buch = [i for i in x_list if i.isalpha()]
    return 