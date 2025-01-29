# given an array, array[0...n-1] of distinct elements
# and a range [low, high], find all numbers in this range
# that are not present in the array

def findMissing(array, low, high):
    for i in range(low, high+1):
        found = False
        for j in range(len(array)):
            if array[j] == i:
                found = True
                break
        if not found:
            print(i)
arr = [1, 3, 4, 6]  # 2, 5, 7, and 8 are missing
low = 1
head = 8
findMissing(arr, low, head)


def findMissing2(array, low, high):
    bag = set(array)
    for i in range(low, high + 1):
        if i not in bag:
            print(i)
arr = [1, 3, 4, 6]  # 2, 5, 7, and 8 are missing
low = 1
head = 8
findMissing(arr, low, head)
