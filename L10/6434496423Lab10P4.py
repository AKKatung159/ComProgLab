#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
drinkdict ={'Cappuccino':[60,70],
            'Espresso':[45,50],
            'Latte':[65,75]}
drink,size,num = input('Enter drink, size and number : ').split()
if drink in drinkdict:
    if size =='S':
        if int(num)>0:
            print('Total :',int(num)*drinkdict[drink][0])
        else:
            print('Incorrect number')
    elif size =='L':
         if int(num)>0:
             print('Total :',int(num)*drinkdict[drink][1])
         else:
             print('Incorrect number')
    else :
        print('Incorrect size.')
else:
    print('Drink not available.')