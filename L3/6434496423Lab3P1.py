"""
@author: Ekkrit Kanchanasiri 6434496423
"""
a, b, c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)
if b**2-4*a*c>=0 and a != 0:
	x1 = ((-b)+((b**2-(4*a*c))**0.5))/(2*a)
	x2 = ((-b)-((b**2-(4*a*c))**0.5))/(2*a)
	print('x =',x1,',',x2)
else :
	print('No real solution.')
