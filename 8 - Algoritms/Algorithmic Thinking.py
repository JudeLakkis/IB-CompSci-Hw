lst = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]


def fixy(lst):
    for nums in range(len(lst)):
        if lst[nums] % 2 == 0:
            lst.append(lst.pop(nums))
            print(lst)
        print(lst)


# for i in range(len(lst)):
#     fixy(lst)

for i in range(len(lst)):
    for nums in range(len(lst)):
        if lst[nums] < 0:
            lst.append(lst.pop(nums))
print(lst)
