#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
training = {'Mike':{'MO':1, 'TU':2, 'FR':3}, 'Got':{'MO':1, 'WE':2, 'FR':1},
'Jane':{'MO':1, 'TH':2, 'FR':3}}
while True:
    inp=input('Enter name and day to get number of training class : ')
    if inp != '0':
        name,date=inp.strip().split()
        if name in [i for i in training] and date in [list(i.keys()) for i in training.values() if i==training[name]][0]:
            print('Number of training class : {}'.format(training[name][date]))
        else:
            print('Not found')
    if inp=='0':
        print('Dictionary of total number of classes : {}'.format({j:sum([list(i.values()) for i in training.values() if i==training[j]][0]) for j in training}))
        break 