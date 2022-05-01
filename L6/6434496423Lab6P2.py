#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:14 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
num = int(input('Enter an integer : '))
print(num,'is divisible by :')
for i in range(1,num+1) :
    if num % i == 0:
        print(i)