#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:  Ekkrit Kanchanasiri 6434496423
"""
w,w_u = input('Weight : ').split()
h,h_u = input('Height : ').split()
w,h =float(w),float(h)
if w_u == 'lbs':
    w /= 2.205
if h_u == 'ft':
    h /= 3.2808399
elif h_u == 'cm':
    h /= 100
BMI = w/(h**2)
if BMI < 18.5 :
	print('ผอม')
elif BMI < 23 :
	print('รูปร่างปกติ')
elif BMI < 25 :
	print('รูปร่างอ้วน')
elif BMI < 30 :
	print('อ้วนระดับที่ 1')
else :
	print('อ้วนระดับที่ 2')
    