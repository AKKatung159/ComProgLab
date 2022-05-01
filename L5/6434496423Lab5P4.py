#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:56:23 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
stu = int(input('Number of student : '))
score = []
spass = []
stupass = 0
stufail = 0
sfail = []
for i in range(1,stu+1):
    s = float(input("Student {number} : ".format(number=i)))
    score.append(s)
    if s >= 5 :
        spass.append(s)
        stupass += 1
    else :
        sfail.append(s)
        stufail += 1
if stu != 0 and stupass != 0 and stufail != 0:
    aver = sum(score)/stu
    averpass = sum(spass)/stupass
    averfail = sum(sfail)/stufail
    maxscore = max(score)
elif stu == 0 :
    aver = 0
    averpass = 0
    averfail = 0
    maxscore = 0
elif stupass == 0:
    aver = sum(score)/stu
    averpass = 0
    averfail = sum(sfail)/stufail
    maxscore = max(score)
elif stufail == 0:
    aver = sum(score)/stu
    averpass = sum(spass)/stupass
    averfail = 0
    maxscore = max(score)
print('Average score :',aver)
print('Average passing score :',averpass)
print('Average failing score :',averfail)
print('Highest score :',maxscore)