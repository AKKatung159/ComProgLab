#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
fee={'G1':{'ปริญญาตรี':{'S1':['16,000','18,000','21,000'],'S2':['4,000','4,500','5,250']},'บัณฑิตศึกษา':{'S1':['22,500','26,000','31,000'],'S2':['6,000','7,000','7,750']}},
     'G2':{'ปริญญาตรี':{'S1':['12,000','14,500','17,000'],'S2':['4,000','4,500','5,250']},'บัณฑิตศึกษา':{'S1':['16,500','19,000','23,000'],'S2':['6,000','7,000','7,750']}}}
y1,y2=['48','49'],['50','51','52','53','54','55']
stuid=input('Enter student ID : ')
if len(stuid)==10 and 48<=int(stuid[0:2]) and 20<int(stuid[8:])<54:
    year,check,group=stuid[0:2],stuid[2],stuid[8:]
    if year in y1:
        year=0
    elif year in y2:
        year=1
    else:
        year=2
    if check=='7':
        check='บัณฑิตศึกษา'
    else:
        check='ปริญญาตรี'
    if group in ['21','23','25','28','30','31','32','33','35','36','37','38','39','53']:
        group='G1'
    else: 
        group='G2'
    sem=input('Enter semester : ')
    if sem in ['1','2','3']:
        if sem in['1','2']:
            sem='S1'
        else:
            sem='S2'
        print('Registation fee :',fee[group][check][sem][year])
    else:
        print('Invalid semester')
else:
    print('Invalid ID')