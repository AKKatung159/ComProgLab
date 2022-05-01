#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
def sum_digits(digit):
    sdigit=[int(i) for i in digit if i.isdigit()]
    return sum(sdigit)

print(sum_digits('zz1xa2d3'))