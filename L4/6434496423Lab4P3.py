#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:  Ekkrit Kanchanasiri 6434496423
"""
id = int(input('Enter student ID : '))
length = len(str(id))
year = id//100000000
fac = id%100
fac1 = [21,23,25,28]
fac2 = [22,24,26,27]
level = id//10000000%10
level1 = [3,4]
level2 = [7]
if length == 10 and 50 <= year and 21 <= fac <= 28 and level in [3,4,7] :
    term = int(input('Enter semester : '))
    term_c1 = [1,2]
    term_c2 = [3]
    if term != [1,2,3]:
        print('Invalidsemester')
    elif (50 <= year <= 55 )and (fac in fac1) and (level in level1) and (term in term_c1):#group1
        print('Registration fee : 18,000')
    elif (50 <= year <= 55 )and (fac in fac1) and (level in level1) and (term in term_c2) :
        print('Registration fee : 4,500')
    elif (50 <= year <= 55 )and (fac in fac1) and (level in level2) and (term in term_c1) :
        print('Registration fee : 26,000')
    elif (50 <= year <= 55 )and (fac in fac1) and (level in level2) and (term in term_c2) :
        print('Registration fee : 7,000')
    elif (56 <= year)and (fac in fac1) and (level in level1) and (term in term_c1) :
        print('Registration fee : 21,000')
    elif (56 <= year)and (fac in fac1) and (level in level1) and (term in term_c2) :
        print('Registration fee : 5,250')
    elif (56 <= year)and (fac in fac1) and (level in level2) and (term in term_c1) :
        print('Registration fee : 31,000')
    elif (56 <= year)and (fac in fac1) and (level in level2) and (term in term_c2) :
        print('Registration fee : 7,750')
    elif (50 <= year <= 55 )and (fac in fac2) and (level in level1) and (term in term_c1) :#group2
       print('Registration fee : 14,500')
    elif (50 <= year <= 55 )and (fac in fac2) and (level in level1) and (term in term_c2) :
       print('Registration fee : 4,500')
    elif (50 <= year <= 55 )and (fac in fac2) and (level in level2) and (term in term_c1) :
       print('Registration fee : 19,000')
    elif (50 <= year <= 55 )and (fac in fac2) and (level in level2) and (term in term_c2) :
       print('Registration fee : 7,000')
    elif (56 <= year)and (fac in fac2) and (level in level1) and (term in term_c1) :
       print('Registration fee : 17,000')
    elif (56 <= year)and (fac in fac2) and (level in level1) and (term in term_c2) :
       print('Registration fee : 5,250')
    elif (56 <= year)and (fac in fac2) and (level in level2) and (term in term_c1) :
       print('Registration fee : 23,000')
    elif (56 <= year)and (fac in fac2) and (level in level2) and (term in term_c2) :
       print('Registration fee : 7,750')
else :
    print('Invalid ID')