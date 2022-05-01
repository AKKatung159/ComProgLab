# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:26:07 2021
@author: Ekkrit
"""
name = input('Enter name : ').strip()
age = int(input('Enter age : '))
print(name+str(((2564-age)%100))+'@chula.ac.th')