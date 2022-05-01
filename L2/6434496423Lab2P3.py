# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 08:05:35 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
a, b, c = input('Length of 3 sides : ').split(',')
a = float(a)
b = float(b)
c = float(c)
print('Triangle :',a+b>c and a+c>b and b+c>a)
