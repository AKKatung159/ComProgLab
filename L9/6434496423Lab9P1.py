#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
print('What would you like to do?\n1: add item\n2: change item\n3: insert item\n4: remove item\n5: show items\n6: exit')
listitem=[]
def add_item(item_list):
    if item_list not in listitem:
        listitem.append(item_list)
        return print('Item has been added')
    else :
        return print('Item is already in the list')
def change_item(item_list):
    if item_list not in listitem:
        return print('Item is not in the list')
    else :
        it2=input('Enter new item : ')
        for i in range(len(listitem)):
            if listitem[i]==item_list:
                listitem.insert(i,it2)
                break
        listitem.remove(item_list)
        return print('Item has been changed')
def insert_item(item_list):
    position=int(input('Enter location that you want to insert : '))
    listitem.insert(position, item_list)
def remove_item(item_list):
    if item_list not in listitem:
        return print('Item is not in the list')
    else :
        listitem.remove(item_list)
        return print('Item has been remove')
def show_item(item_list):
    if len(listitem)==0:
        return print('The list is currently empty')
    else :
        return print(listitem)
    
    
    
while True:
    menu=int(input('Enter a number : '))
    if menu==1:
        it=input('Enter item : ')
        add_item(it)
    if menu==2:
        it2=input('Enter item you want to change : ')
        change_item(it2)
    if menu==3:
        it3=input('Enter item you want to insert : ')
        insert_item(it3)
    if menu==4:
        it4=input('Enter item you want to remove : ')
        remove_item(it4)
    if menu==5:
        show_item('')
    if menu == 6:
        break