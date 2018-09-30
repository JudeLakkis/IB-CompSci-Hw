import random
import math

# Task 1
a = 10
b = 20
c = 30


def foo1(a, b):
    a = b + c
    print(a)


def foo2(b, c):
    b = a + c
    print(b)


def foo3(a, c):
    c = a + b
    print(c)

# foo1(3,4)
# foo2(5,6)
# foo3(7,8)
# foo1(foo2(1,2), foo3(3,4))

# Task 2


def foo1_fixed(a):
    global b
    a = b + c
    print(a)


foo1_fixed(a)

# Task 3
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)


def add(num1, num2):
    print(num1 + num2)
    return num1 + num2


def triple(num3):
    print(add(num3, num3))
    return num3, add(num3, num3)


def quadruple(num3):
    a = triple(num3)
    return add(a, num3)


add(num1, num2)
triple(num3)

# Task 4/6/7/8
# See main.py and module1.py

# Task 9
print(math.sqrt(9))
# Returns the square root of x
print(math.factorial(5))
# Returns the factorial of x
print(math.isfinite(12))
# Returns True if x is neither an infinity nor a NaN (Not a Number)
print(math.ldexp(2, 2))
# Returns x * (2**i)
print(math.sin(-30))
# Returns the sine of x


# Task 10
# Uses the one created in the file rather than the imported one
