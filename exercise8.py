# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:17:38 2023

@author: s_gastaud21
""" 
 
satz = "Hallo, Berlin"
satz_list = list(satz)
vokale = ["a", "e", "i", "o", "u", "y"]
konsonanten_zählen = 0
vokon_zählen = 0
    
for b in satz_list:
    if satz.isalpha():
        if b in vokale:
            vokon_zählen += 1
        else: 
            konsonanten_zählen += 1
            
            
print(konsonanten_zählen)
print(vokon_zählen)


def vokon_zählen(x):
    wort = x
    count_buch = 0
    count_vok = 0
    vokalen = "aeiou"
    
    for i in wort:
        if i.isalpha():
            count_buch += 1
            if i in vokalen:
                count_vok += 1
            
    print(f"Es gibt {count_vok} Vokalen und {count_buch-count_vok} Konsonanten")
    
vokon_zählen("Hello, Berlin")