# from random import uniform, randint
# import string
# mylist = [7, 2, 3, 4, 5]
# print(mylist.index(7))

# print("%.2f" % uniform(1.3, 1.5))
# var1 = 0
# var2 = 25
# print(string.ascii_lowercase[12])
# print(string.ascii_lowercase[randint(var1, var2)])

count = 0
while count < 10:
    print(count * 10)
    count += 1

total = 3
while total > -5.2:
    print('%.2f' % total)
    total -= 0.2


for i in range(0, 101):
    if i % 3 == 0:
        print('', end='')
    elif i % 8 == 0:
        print('', end='')
    else:
        print(i)

height = 5
for i in range(height):
    print(('*' * i))
