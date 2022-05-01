#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:18:03 2021

@author: akkatung
"""
element=[]
table = open('periodic_table.txt',encoding='UTF-8')
for ele in table :
    at_num,th_name,en_name,sym,mass,group,period = ele.split()
menu = ('*** โปรแกรมการคำนวณสารละลาย ***\n\t1 ข้อมูลสาร\n\t2 คำนวณหามวลของสารในหน่วยกรัม\n\t3 คำนวณหาจำนวนโมลของสาร\n\t4 คำนวณหาจำนวนโมลาริตีของสาร\n\t5 คำนวณหาจำนวนโมแลลิตีของสาร\n\t6 คำนวณหาปริมาตรของสารในหน่วยลิตร\n\t7 คำนวณหาความหนาแน่นของสาร\n\t0 ออกจากโปรแกรม')
print(menu)
calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
while 0 <= calcu <= 7 :
    if calcu == 1 :
        print('โปรแกรมแสดงข้อมูลสาร')
        ele_ip = input('ระบุชื่อสาร : ')
        table = open('periodic_table.txt',encoding=("UTF-8"))
        for ele in table:
            at_num,th_name,en_name,sym,mass,group,period = ele.split()
            if ele_ip == sym :
                print('สัญลักษณธาตุคือ ',sym,'\tเลขมวล\t\t',mass,'\n\t\t\t\tเลขอะตอม\t\t',at_num,'\n\t\t\t\tชื่่อภาษาไทย\t',th_name,'\n\t\t\t\tชื่อภาษาอังกาษ\t',en_name,'\n\t\t\t\tหมู่\t\t\t',group,'\n\t\t\t\tคาบ\t\t\t',period)
        table.close()
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 2 :
        print('โปรแกรมคำนวณหามวลของสารในหน่วยกรัม')
        ele_ip = input('ระบุชนิดของสาร : ')
        mole_ip = float(input('ระบุจำนวนโมลของสาร : '))
        table = open('periodic_table.txt')
        for ele in table:
            at_num,th_name,en_name,sym,mass,group,period = ele.split()
            if ele_ip == sym :
                print(sym,'มีมวล =',mole_ip*float(mass),'กรัม')
        table.close()
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 3 :
        print('โปรแกรมคำนวณหาจำนวนโมลของสาร')
        ele_ip = input('ระบุชนิดของสาร : ')
        mass_ip = float(input('ระบุจำนวนมวลของสารในหน่วยกรัม : '))
        table = open('periodic_table.txt')
        for ele in table:
            at_num,th_name,en_name,sym,mass,group,period = ele.split()
            if ele_ip == sym :
                print(sym,'มีจำนวนโมล =',mass_ip/float(mass),'โมล')
        table.close()
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 4 :
        print('โปรแกรมคำนวณหาจำนวนโมลาริตีของสาร')
        mole_ip = float(input('ระบุจำนวนโมลของตัวถูกละลาย : '))
        volum_ip = float(input('ระบุปริมาตรของสารละลายในหน่วยลิตร : '))
        print('จำนวนโมลาลิตีของสาร =',mole_ip/volum_ip,'โมลต่อลิตร')
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 5 :
        print('โปรแกรมคำนวณหาจำนวนโมแลลิตีของสาร')
        mole_ip = float(input('ระบุจำนวนโมลของตัวถูกละลาย : '))
        weight_ip = float(input('ระบุน้ำหนักของตัวทำละลายในหน่วยกิโลกรัม : '))
        print('จำนวนโมแลลิตีของสาร =',mole_ip/weight_ip,'โมลต่อกิโลกรัม')
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 6 :
        print('โปรแกรมคำนวณหาปริมาตรของสารในหน่วยลิตร')
        mass_ip = float(input('ระบุจำนวนมวลของสารในหน่วยกรัม : '))
        den_ip = float(input('ระบุความหนาแน่น : '))
        print('ปริมาตรของสาร =',mass_ip/den_ip,'ลิตร')
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    elif calcu == 7 :
        print('โปรแกรมคำนวณหาความหนาแน่นของสาร')
        mass_ip = float(input('ระบุจำนวนมวลของสารในหน่วยกิโลกรัม : '))
        vol_ip = float(input('ระบุจำนวนปริมาตรของสารในหน่วยลิตร : '))
        print('ความหนาแน่นของสาร =',mass_ip/vol_ip,'กิโลกรัมต่อลิตร')
        print(menu)
        calcu = int(input('ระบุรูปแบบการคำนวณที่ท่านต้องการ : '))
        continue
    else :
        print('สิ้นสุดโปรแกรม')
        break
if calcu < 0 or calcu > 7:
    print('ไม่พบโปรแกรมคำนวณที่ท่านต้องการ')