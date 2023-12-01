# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:10:18 2023

@author: s_gastaud21
"""

def buchstaben_häufigkeit(word):
    res = {}
    sorted_word = sorted(word.lower())
    for letter in sorted_word:
        if letter.isalpha():
        #if letter not in "abcdefghijklmnopqrstuvwxyz":
            #continue
            if letter in res:
                res[letter] += 1
            else:
                res[letter] = 1
            
    return res

print(buchstaben_häufigkeit("Hallo558"))
            
            
            