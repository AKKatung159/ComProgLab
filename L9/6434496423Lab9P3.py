#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
x=int(input('Enter a num ber between [0,9] : '))
xlist=[i for i in range(2,100) if str(x) in str(i)]
if x!=0:
    print(xlist)
if x==0:
    print([i for i in range(2,10)]+xlist)