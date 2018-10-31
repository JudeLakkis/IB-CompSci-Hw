def foo(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            print('True')
            return True
        print('False')
    print('False')
    return False


nums = [1, 2, 3, 4, 5, 6]
foo(nums)
