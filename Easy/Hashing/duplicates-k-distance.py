def duplicatesKDistance(arr, k):
    bag = {}
    for idx, val in enumerate(arr):
        if val in bag:
            if idx - bag[val] <= k:
                return True
        bag[val] = idx
    return False


print(duplicatesKDistance([1, 2, 3, 1, 4, 5], 3))
print(duplicatesKDistance([1, 2, 3, 4, 1, 5], 3))
print(duplicatesKDistance([1, 2, 1, 3, 4], 3))
