#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
vectors = open('vectors.txt')
vec1=[float(i) for i in vectors.readline().split()]
vec2=[float(i) for i in vectors.readline().split()]
print('v1 = {}\nv2 = {}'.format(vec1,vec2))
if len(vec1) == len(vec2):
    total=0
    for i in range(len(vec1)):
       total += vec1[i]+vec2[i] 
    print('v1*v2 =',total)
else :
    print('Incompatible size')
vectors.close()