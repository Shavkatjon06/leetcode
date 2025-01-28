# find the max distance between two occurrences

def maxDistance(arr1):  # strategy 1
    result = 0
    for i, x in enumerate(arr1):
        for j in range(i+1, len(arr1)):
            if x == arr1[j] and j-i > result:
                result = j-i
    return result


print(maxDistance([1, 1, 2, 2, 2, 1]))


def maxDistance2(arr1):  # strategy 2
    result = 0
    bag = {}
    for idx, val in enumerate(arr1):
        if val in bag:
            if idx - bag[val] > result:
                result = idx - bag[val]
        else:
            bag[val] = idx
    return result


print(maxDistance2([1, 1, 2, 2, 2, 1]))
