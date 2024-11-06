def rotate(nums, k):
    length = len(nums)  # getting the length, [1,2,3,4] => 4
    for x in range(k):  # repeat k times
        last = nums[length - 1]  # get the last element, [1,2,3,4] => 4
        for i in range(length - 1, 0, -1):  # if array is [1,2,3,4], length is 4, so i is 3
            nums[i] = nums[i - 1]  # nums[3] which is 4 is now equal to nums[2]. we have element 3 at index 2
        nums[0] = last  # after loop, change the first element to last
    return nums

print(rotate([1,2,3,4,5,6,7], 3))
