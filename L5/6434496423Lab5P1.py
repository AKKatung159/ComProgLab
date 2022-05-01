#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:56:14 2021

@author: Ekkrit Kanchanasiri 6434496423
""" 
name = input('Enter username : ').strip()
while name != 'Ekkrit':
    name = input('Incrrect. Enter again : ').strip()
print('Hello,',name)