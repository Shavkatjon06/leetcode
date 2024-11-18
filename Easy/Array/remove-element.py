def removeElement(nums, target):
    left = 0  # This is the index where we put numbers that aren't the target
    for i in range(len(nums)):  # Go through each item in the list
        if nums[i] != target:  # If the number isn't the target we want to remove
            nums[left] = nums[i]  # Put the number at the current 'left' index
            left += 1  # Move 'left' forward to the next spot
    return left  # Return how many numbers are left after removing the target


print(removeElement([3, 2, 2, 3], 3))
