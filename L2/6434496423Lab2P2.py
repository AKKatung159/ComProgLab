# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 08:05:32 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
a, b, c = input('Enter coefficients a, b, c: ').split(',')
a = float(a)
b = float(b)
c = float(c)
print('Can use quadratic formula :',b**2-4*a*c>=0 and a!=0)