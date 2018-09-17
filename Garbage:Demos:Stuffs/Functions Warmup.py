my_str = 'Peter Retard'
my_float = 3.14
my_int = 0
my_bool = True

print(type(my_bool))
print(type(my_int))
print(type(my_float))
print(type(my_str))

print(bool(my_int))
print(bool(my_float))

print(int(my_bool)+ int(my_float))

print(hex(my_int))
print(bin(my_int))

print(chr(69))
print(ord('E'))
# Converts back and forth between ASCII Code

# globals().__setitem__('my_float', 0)

print(my_int)

a = 2
for i in range(20):
	a **= 2
print(a)
