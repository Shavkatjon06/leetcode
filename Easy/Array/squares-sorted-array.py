def sortedSquares(nums):
    nums = [i ** 2 for i in nums]
    nums.sort()
    return nums


print(sortedSquares([-4,-1,0,3,10]))
