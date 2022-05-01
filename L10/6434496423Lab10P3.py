#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
def fucscore(key):
    return stuscore[key]

f = open('studentScore.txt')
stuscore={}
for l in f:
    name,score = l.split()
    stuscore[name]=score
f.close()
[print(i) for i in sorted(stuscore.keys(), key=fucscore ,reverse=True)]