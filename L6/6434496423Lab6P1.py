#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:12 2021

@author: Ekkrit Kanchanasiri 6434496423
"""
word = input('Next word : ')
all_word = ''
while word != '.' :
    all_word += word+' '
    word = input('Next word : ')
print('Sentence :',all_word)