#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ekkrit Kanchanasiri 6434496423
"""
solf = open('sol.txt')
examf = open('exam.txt')
sol = [i for i in solf.readline().split()]
exam = [i.split() for i in examf]
solf.close()
examf.close()
score=[]
scoreavg=[]
minsc=''
maxsc=''
for i in range(len(exam)):
    total=0
    for j in range(len(sol)):
        if sol[j]==exam[i][j]:
            total+=1
    score.append(total)
print('student score :\n{}'.format(score))
for i in range(len(sol)):
    total=0
    for j in range(len(exam)):
        if sol[i] == exam[j][i]:
            total+=1
    scoreavg.append(total/len(exam))
    print('Question',i+1,'\t:',scoreavg[i])
minscore=[str(i+1) for i in range(len(sol))if scoreavg[i]==max(scoreavg)]
maxscore=[str(i+1) for i in range(len(sol))if scoreavg[i]==min(scoreavg)]
for i in range(len(minscore)):
    minsc+=str(minscore[i])+' '
for i in range(len(maxscore)):
    maxsc+=str(maxscore[i])+' '
print('{}is the hardest question.\n{}is the easiest question.'.format(maxsc,minsc))