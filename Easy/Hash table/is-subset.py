# check if an array is subset of another array

def isSubset(arr1, arr2):
    bag = {}
    for i in arr1:
        bag[i] = True
    for i in arr2:
        if i not in bag:
            return False
    return True


print(isSubset([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print(isSubset([10, 5, 2, 23, 19], [19, 5, 3]))
# time complexity O(len(arr1) + len(arr2))
# Auxiliary Space O(len(arr1))
