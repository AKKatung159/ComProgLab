#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:56:23 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
balance = 50000
wit = int(input('Withdraw : '))
while balance >= wit:
    balance -= wit
    if balance == 0:
        print('Balance is 0.')
        break
    wit = int(input('Withdraw : '))
else:
    print('Insufficient fund.')