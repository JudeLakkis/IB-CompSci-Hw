from random import random, randint

# Task 1
nums = {i: 0 for i in range(10)}

for i in range(10000):
    nums[randint(0, 9)] += 1
print(nums)
print('\n\n')

# Task 2
flts = {i: [] for i in range(10)}

for i in range(10000):
    n = random() * 10
    flts[int(n)].append(n)
print(flts)
