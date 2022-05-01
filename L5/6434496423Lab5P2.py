#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:56:22 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
count = 1
name = input('Enter username : ').strip()
while name != 'Ekkrit' and count <= 2:
    name = input('Incrrect. Enter again : ').strip()
    count += 1
if name == 'Ekkrit':
    print('Hello,',name)
else :
    print('Not allowed. Incorrect name.')