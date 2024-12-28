def containsNearbyDuplicate(nums, k):
    bag = {}
    for i, num in enumerate(nums):
        if num in bag and abs(i - bag[num]) <= k:
            return True
        bag[num] = i
    return False


array = [1, 2, 3, 1]
x = 3
print(containsNearbyDuplicate(array, x))
array = [1, 2, 3, 1, 2, 3]
x = 1
print(containsNearbyDuplicate(array, x))