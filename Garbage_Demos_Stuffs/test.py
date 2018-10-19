add, threes = 0, 0
for i in range(199, 401):
    if i % 3 == 0:
        threes += i
    add += i
print(add - threes)
