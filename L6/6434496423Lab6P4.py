#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:15 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
templs = 0
for i in range(1,8):
    temp = float(input('Day {day} : '.format(day=i)))
    if temp < templs:
        print('Temperature dropped on day',i)
    templs = temp