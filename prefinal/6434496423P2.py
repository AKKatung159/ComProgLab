#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
village = [('zone1', 'S', 20), ('zone1', 'M', 10), ('zone1', 'L', 5), ('zone2', 'S', 20), ('zone2', 'M', 25), ('zone3', 'L', 20)]
inp=input('Enter a zone name to view data : ')
a = [i[0] for i in village]
b = [(i[1],i[2]) for i in village]
showls=[]
total=0
if inp in a:
    for i in range(len(a)):
        if inp ==a[i]:
            showls.append(b[i])
            total+=b[i][1]
    print('List of houses in {} : {}\nThere are {} sizes of house in {}\nThere are {} houses in {}'.format(inp,showls,len(showls),inp,total,inp))
else:
    print('Not found')