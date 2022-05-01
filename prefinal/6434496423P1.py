#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
f=open('inc_exp.txt')
ls=[]
lscheck=[]
for l in f:
    month,income,expense = l.strip().split()
    ls.append([int(income),int(expense),int(income)-int(expense)])
    lscheck.append(int(income)-int(expense))
f.close()
inp = int(input('Enter month number to get income and expense : '))
if 0<inp<=12:
    print('Month {} income = {} expense = {} balance = {}'.format(inp,ls[inp-1][0],ls[inp-1][1],ls[inp-1][2]))
    print('Max balance = {} is in month {}'.format(max(lscheck),*[i+1 for i in range(len(lscheck)) if lscheck[i]== max(lscheck)]))
else:
    print('Month ont found')