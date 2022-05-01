#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
f,j = open('conversation.txt'),''
for i in f:
    j+=i
f.close()
check ={word.strip('?:.,'):0 for word in j.split()}
checkls =[word.strip('?:.,') for word in j.split()]
for x in check:
    for y in checkls:
        if x==y:
            check[x]+=1
    print(x,check[x])