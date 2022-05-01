#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
import math as m
shape = input('Choose circle, square or rectangle : ')
if shape == 'circle':
    r = float(input('Length of the radius of the circle : '))
    print('Area is',m.pi*r*r)
elif shape == 'square':
    sq_side = float(input('Length of the side of the square : '))
    print('Area is',sq_side*sq_side)
elif shape == 'rectangle':
    side1,side2 = input('Length of two side of the rectangle : ').split(',')
    print('Area is',float(side1)*float(side2))
else :
    print('Invalid choice')