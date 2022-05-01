#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
items={}
for i in range(10):
    idpd,size,num = input('Enter product ID, size, number of items : ').strip().split()
    key=idpd + ' ' + size
    if (key) in items:
        items[key]=items[key]+int(num)
    else:
        items[key]=int(num)
print('Stocks :')
[print(i,items[i]) for i in items]