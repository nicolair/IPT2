# -*- coding: utf-8 -*-
texte = "If Youth, throughout all history, had had a champion to stand up for\
 it; to show a doubting world that a child can think; and, possibly, do it\
 practically; you wouldn't constantly run across folks today who claim that\
 \"a child don't know anything.\" A child's brain starts functioning at birth;\
 and has, amongst its many infant convolutions, thousands of dormant atoms,\
 into which God has put a mystic possibility for noticing an adult's act, and\
 figuring out its purport."

Mots = []
mot = ""
for c in texte :
    if c == " ":
        Mots.append(mot)
        mot = ""
    else:
        mot = mot + c
        
print(Mots)
