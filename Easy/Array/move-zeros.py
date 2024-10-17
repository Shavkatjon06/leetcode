# move zeros
def moveZeros(nums):
    left = 0  # to keep track the index number to put elements to our nums
    for i in range(len(nums)):  # loop through our nums
        if nums[i] != 0:  # if our element is not zero
            nums[left] = nums[i]  # we will put it to left-index number
            left += 1  # increment left by one
    for i in range(left, len(nums)):  # make the rest of the nums 0s
        nums[i] = 0
    return nums
print(moveZeros([0,1,0,3,12]))