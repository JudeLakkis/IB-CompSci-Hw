from random import randint

num = randint(1, 10)


i = None
fin = 0
print(num)

if isinstance(num, int):
    if num >= 1:
        i = 2
else:
    print('Nope')


for j in range(20):
    if fin == 1:
        break
    if num == i:
        print('Number is: ', num)
        print('It is a prime')
        fin = 1
    else:
        num2 = num % i
        if num % i == 0:
            print('Number is: ', num)
            print('The input number is not a prime')
            fin = 1
