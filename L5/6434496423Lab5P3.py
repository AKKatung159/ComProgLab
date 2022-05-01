#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:56:22 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
stu = int(input('Number of student : '))
score = []
for i in range(1,stu+1):
    s = input("Student {number} : ".format(number=i))
    score.append(s)