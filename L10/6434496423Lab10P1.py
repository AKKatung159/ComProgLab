#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
subject = {'2301117':['Calculus I',4],
           '2301118':['Calculus II',4],
           '2301286':['Probability and Statistics',3],
           '2301399':['Project Proposal',1],
           '2301499':['Senior Project',2],
           '2302113':['General Chemistry Lab I',1],
           '2302161':['General Chemistry',3]}
check = input('Course ID : ')
check=check.strip()
while check!='0':
    if check in subject:
        print(*subject[check])
    else:
        print('Unknow')
    check = input('Course ID : ')