# Реализуйте алгоритм перемешивания списка.

import os
os.system('cls')


def sort(nums):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted = True


nums = [5, 3, 7, 1, 9]
sort(nums)
print(nums)
