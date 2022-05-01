"""
@author: Ekkrit Kanchanasiri 6434496423
"""
id = input('Enter student ID : ')
n_3={3,4,7}
if len(id)== 10 and 50<=(int(id)//100000000)<=64 and ((int(id)//10000000)%10)in n_3 and 21<=int(id)%100 <=28:
	print('Valid ID')
else :
	print('Invalid ID')
