#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:17:10 2021

@author: akkatung
"""
'''
score = 0
student_score = []
Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10 = 0,0,0,0,0,0,0,0,0,0
Q =[]
f1 = open('sol.txt')
sol = f1.readline().split()
f1.close()
minQQ=''
maxQQ=''
f2 = open('exam.txt')
for exam in f2:
    exam = exam.split()
    for i in range(len(exam)):
        if exam[i]==sol[i]:
            score += 1 
            if i==0:
                Q1 += 1
            elif i ==1:
                Q2 += 1
            elif i ==2:
                Q3 += 1
            elif i ==3:
                Q4 += 1
            elif i ==4:
                Q5 += 1
            elif i ==5:
                Q6 += 1
            elif i ==6:
                Q7 += 1
            elif i ==7:
                Q8 += 1
            elif i ==8:
                Q9 += 1
            elif i ==9:
                Q10 += 1
    student_score.append(score)
    score = 0
QQ = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]
print('Student score: \n'+str(student_score))
for q in range(len(sol)):
    print('Question',q+1,':',QQ[q]/8)
for i in range(len(QQ)):
    if QQ[i] == min(QQ):
        minQQ+=str(i+1)+' '
    if QQ[i] == max(QQ):
        maxQQ+=str(i+1)+' '
print(minQQ,'is the hardest question.')
print(maxQQ,'is the easiest question.')
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input().split()
for i in range(9):

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for j in range(len(l)):
        if int(l[j][0]) == i+1 :
            print("{}|{}".format(i+1,l[j][1]))
            continue
        if int(l[j][0]) != i+1:
            print("{}|".format(i+1))