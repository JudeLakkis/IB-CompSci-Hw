from random import randint
wheel = [str(i) for i in range(37)]
wheel.append('00')

odd = wheel[1:36:2]
even = wheel[2:36:2]
money = 1000


for i in range(10):
    betted = money / 5
    landed = randint(0, len(wheel))


print(odd)
print(even)
print(wheel)
