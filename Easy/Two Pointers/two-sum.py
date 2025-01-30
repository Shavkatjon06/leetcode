def twoSum(array, target):
    length = len(array)
    for i in range(length):
        for j in range(i+1, length):
            if array[i] + array[j] == target:
                return True
    return False


print(twoSum([10, 15, 20, 5], 30))
print(twoSum([10, 15, 20, 5], 50))


# Two Pointer Technique is the best solution for this problem that works well for sorted arrays.
def twoSum2(array, target):
    left, right = 0, len(array)-1
    while left < right:
        sum = array[left] + array[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False


print(twoSum2([-8, 1, 4, 6, 10, 16], 16))
