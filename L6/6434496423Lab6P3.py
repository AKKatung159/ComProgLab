#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:14 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
num = int(input('Enter an integer : '))
if num % 2 == 0 and num != 2 or num == 0 or num == 1 :
    print(num,'is not a prime number.')
else :
    divisor = 3
    while divisor <= num ** 0.5 :
        if num % divisor == 0:
            print(num,'is not a prime number.')
            break
        divisor += 2
    else :
        print(num,'is a prime number.')