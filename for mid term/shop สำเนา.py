#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 03:49:50 2021

@author: akkatung
"""
price_tot = 0
pd_tot = '' 
pd_list = open('product_list.txt') 
print('*** ตู้กดสินค้าอัตโนมัติ ***')
num,pd,price = pd_list.readlines().split(':')


'''
for pd in pd_list :
    num,pd,price = pd.split(':')
    print(num,'\t',pd,'\t\t',price,'\n')
pd_list.close()
'''
'''
product = int(input('กรุณาระบุหมายเลขสินค้าที่ท่านต้องการค่ะ : '))
while 0 < product < int(num):
    item = int(input('ระบุจำนวนสินค้าที่ท่านต้องการค่ะ : '))
    pd_list = open('product_list.txt') 
    for pd in pd_list :
        num,pd,price = pd.split(':')
        if product == int(num) :
            price_tot+= (int(price)*item)
            pd_tot+=(pd+'\t'+str(item)+' ชิ้น\n')
    pd_list.close()
    check = input('ท่าต้องการซื้อสินค้าต่อหรือไม่ Y/N : ')
    if check == 'Y':
        product = int(input('กรุณาระบุหมายเลขสินค้าที่ท่านต้องการค่ะ : '))
        continue
    elif check == 'N' :
        print('รายการสินค้าทั้งหมด\n',pd_tot)
        print('รวมเป็นเงินทั้งสิ้น :',price_tot,'บาท\n*** ขอบคุณที่ใช้บริการค่ะ ***')
        break
    else :
        break
if 0 >= product or product > int(num):
    print('ไม่พบหมายเลขที่ท่านต้องการค่ะ')
    '''