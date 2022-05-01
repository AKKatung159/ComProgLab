#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:12 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
x,y = input('Intial position : ').split(',')
x,y=int(x),int(y)
move = open('move.txt')
for line in move:
    line = line.strip()
    if line == 'U':
        y+=1
    elif line == 'D':
        y-=1
    elif line == 'L':
        x-=1
    elif line == 'R':
        x+=1
    else :
        print('Invalid command')
move.close()
print('Robot stops at',x,',',y)