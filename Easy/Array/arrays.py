# reverse an array
# def reverse(nums):
#   new = []
#   for i in range(len(nums)):
#     new.append(nums.pop())
#   return new
# print(reverse([3,5,7,8]))


# find largest element
# def largest(nums):
#     largest = 0  # a variable to store the largest element
#     for i in nums:  # loop through the elements
#         if i > largest:  # if 3 > 0, largest is 3. if 56 > 3, largest = 56 etc...
#             largest = i  # largest is i
#     return largest
# print(largest([3,56,4,2]))


# find the second-largest element strategy-1
# def secondLargest(nums):
#     length = len(nums)
#     nums.sort()
#     for i in range(length - 2, -1, -1):
#         if nums[i] != nums[length - 1]:
#             return nums[i]
#     return -1
# print(secondLargest([3,9,7,13,2,13]))


# find the second-largest element strategy-2
# def secondLargest(nums):
#     length = len(nums)  # get the length of array
#     largest = -1  # to store the largest element
#     secondLargest = -1  # to store the second-largest element
#     for i in range(length):
#         if nums[i] > largest:  # if current element is greater than largest
#             secondLargest = largest  # store the previous largest value
#             largest = nums[i]  # update the largest value
#         elif nums[i] < largest and nums[i] > secondLargest:  # if current is less than largest but greater than second-largest
#             secondLargest = nums[i]  # update second-largest
#     return secondLargest
# print(secondLargest([3,9,7,12,2,9]))


# check if array is sorted
# def checkSorted(nums):
#     if len(nums) <= 1:  # if array has 1 element, no need to check
#         return True
#     for i in range(1, len(nums)):  # start looping from the 1st element
#         if nums[i-1] > nums[i]:  # if prev is greater than current
#             return False  # it's not sorted
#     return True
# print(checkSorted([20, 23, 23, 45, 88]))  # True
# print(checkSorted([7, 9, 11, 3]))  # False


# rotate an array
# def rotateLeft(nums):
#     if len(nums) > 0:
#         first = nums[0]
#         for i in range(len(nums)-1):
#             nums[i] = nums[i+1]
#         nums[-1] = first
#     return nums
# print(rotateLeft([1,2,3,4]))