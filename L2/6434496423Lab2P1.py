# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 07:57:55 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
a, b, c = input('Enter coefficients a, b, c: ').split(',')
a = float(a)
b = float(b)
c = float(c)
x1 = ((-b)+((b**2-(4*a*c))**0.5))/(2*a)
x2 = ((-b)-((b**2-(4*a*c))**0.5))/(2*a)
print('x =',x1,',',x2)