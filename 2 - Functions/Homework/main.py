import module1
from module1 import say_hello
from math import sqrt


print(module1.var1)

name = 'Sam'


def say_hello(name):
    print(name, 'smells bad!')


def sqrt(num):
    return num**0.5


say_hello(name)
say_hello('Tim')
print(sqrt(9))
