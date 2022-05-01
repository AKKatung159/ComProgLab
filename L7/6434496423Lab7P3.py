#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:14 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact
def summation(a,b):
    func=0
    for num in range(a,b+1):
        func+= 1/fact(num)
    return func
m = int(input('Enter m : '))
n = int(input('Enter n : '))
if m < n :
    print(summation(m, n))
elif m > n :
    print(summation(n, m))