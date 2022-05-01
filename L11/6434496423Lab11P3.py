#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
f = open('score.txt')
stuscore={}
for l in f:
    name,s1,s2,s3,s4 = l.split()
    stuscore[name]=int(s1)+int(s2)+int(s3)+int(s4)
f.close()
lssc=[i for i in stuscore.values()]
lssc.sort(reverse=True)
print('The winners are :')
for i in range(3):
    for j in stuscore:
        if stuscore[j]==lssc[i]:
            print(i+1,':',j,lssc[i])