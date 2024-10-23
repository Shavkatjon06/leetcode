def mergeArrays(arr1, arr2):
    n, m = len(arr1), len(arr2)  # let's take their lengths
    i = j = 0  # we will take elements in these indexes and compare
    result = []  # we will create a new array
    while i < n and j < m:  # while index is less than len(array), for example: len(arr1) = 4, len(arr2) = 6
        if arr1[i] < arr2[j]:  # if arr[0] is less than arr2[0]
            result.append(arr1[i])  # then add
            i += 1  # increment by one, arr1[1]
        else:
            result.append(arr2[j])
            j += 1  # do the same
    # arr1 = [1,2,3] while arr1[5,8,9,10,11] or vice versa, then we have to add the rest elements 10,11 from arr
    while i < n:
        result.append(arr1[i])
        i += 1
    while j < m:
        result.append(arr2[j])
        j += 1
    return result


print(mergeArrays([1,2,3], [3,4,5]))
print(mergeArrays([1,2,3], []))