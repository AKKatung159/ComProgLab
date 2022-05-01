#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:14 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
x,y = input('Intial position : ').split(',')
x,y=int(x),int(y)
move = open('move.txt')
for line in move:
    line = line.strip()
    if line == 'U' and y<9:
        y+=1
    elif line == 'D'and y>-9:
        y-=1
    elif line == 'L' and x>-9:
        x-=1
    elif line == 'R' and x<9:
        x+=1
    elif line not in ['U','D','L','R'] :
        print('Invalid command')
move.close()
print('Robot stops at',x,',',y)