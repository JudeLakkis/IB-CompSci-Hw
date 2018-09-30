# https://www.cemc.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf

x = int(input('Enter X co-ordinate:\n-> '))
y = int(input('Enter Y co-ordinate:\n-> '))


if x and y > 0:
	print('Quadrant 1')
if x < 0 and y > 0:
	print('Quadrant 2')
if x > 0 and y < 0:
	print('Quadrant 3')
if x and y < 0:
	print('Quadrant 4')