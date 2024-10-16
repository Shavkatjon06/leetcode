# reverse an array
# def reverse(nums):
#   new = []
#   for i in range(len(nums)):
#     new.append(nums.pop())
#   return new
# print(reverse([3,5,7,8]))


# middle of 2 arrays in a new array
# def middle(a, b):
#     mid1 = len(a) // 2
#     mid2 = len(b) // 2
#     return [a[mid1], b[mid2]]
# print(middle([3,4,5], [6,7,8]))


# sum of array
# from functools import reduce
# def add(a,b):
#     return a+b
# result = reduce(add, [1,2,3,4,5])
# print(result)


# find largest element and convert all elements to largest
# def largest(nums):
#     largest = 0
#     for i in nums:
#         if i > largest:
#             largest = i
#     nums = [largest for i in nums]
#     return nums
# print(largest([3,56,4,2]))


# rotate an array #strategy_1
# def rotateLeft1(nums):
#     if len(nums) == 0:
#         return False
#     return nums[1:] + [nums[0]]
# print(rotateLeft1([1,2,3,4,5,6]))


# rotate an array #strategy_2
# def rotateLeft2(nums):
#     if len(nums) > 0:
#         first = nums[0]
#         for i in range(len(nums)-1):
#             nums[i] = nums[i+1]
#         nums[-1] = first
#     return nums
# print(rotateLeft2([1,2,3,4]))