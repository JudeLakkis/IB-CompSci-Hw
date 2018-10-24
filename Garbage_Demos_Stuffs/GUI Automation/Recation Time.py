from itertools import cycle
cat = 'meow'
dog = 'bark'
a = cycle([cat, dog])

for i in range(10):
    print(next(a))
