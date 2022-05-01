#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:16 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
'''
import random
num = random.randint(1,9)
#print(num)
guess = int(input('Your guess : '))
while guess != num :
    guess = int(input('Your guess : '))
if guess == num :
    print('Correct.')
    '''
'''
hour = int(input('Enter Hour : '))
day = hour//24
minute = (hour%24)*60
print(hour,'hour is',day,'day',minute,'minute')
'''
'''
x1=float(input('Enter X1 : '))
y1=float(input('Enter Y1 : '))
x2=float(input('Enter X2 : '))
y2=float(input('Enter Y2 : '))
print('Distance is',((x1-x2)**2+(y1-y2)**2)**0.5)
'''
'''
name = input('Enter your name : ')
year = int(input('Enter your year of birth : '))
print('Your user name is',name+str((year-243)%100))
'''