x, y = 200, 200

def add_100(x):
	x += 100
	# print(x)
	return x

def mins_100(y):
	y -= 100
	# print(y)
	return y

add_100(x)
mins_100(y)
print(add_100(x) + mins_100(y))

