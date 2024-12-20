def firstLast(arr, target):
    length = len(arr)
    first = -1
    last = -1
    for i in range(length):
        if target != arr[i]:  # if it's not target, continue
            continue
        if first == -1:  # update when we find an element for the first time
            first = i
        last = i  # always update last whenever we find an element
    return [first, last]


result = firstLast([1,2,2,2,3,4,7,8,8], 1)
print(result)  # [0, 0], first and last position at index 0

result = firstLast([1,2,2,2,3,4,7,8,8], 2)
print(result)  # [1, 3], first and last position at index 1 and 3
