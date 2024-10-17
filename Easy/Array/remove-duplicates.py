def removeDuplicates(nums):
    left = 1  # 'left' starts at index 1 because the first element is already considered distinct
    for right in range(1, len(nums)):  # Start from the second element and iterate to the second-last element
        if nums[right] != nums[right - 1]:  # If the current element is different from the previous one
            nums[left] = nums[right]  # Move the current distinct element to the 'left' position
            left += 1  # Increment 'left' to point to the next position for a new distinct element
    return left  # the length of the array with distinct elements


print(removeDuplicates([1, 1, 2]))