"""
@author: Ekkrit Kanchanasiri 6434496423
"""
weight = float(input('weight (kg.) : '))
hight = float(input('hight (m.) : '))
BMI = weight/(hight**2)
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
