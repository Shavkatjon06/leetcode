# brute-force approach that uses nested loops to iterate
def twoSum(list, target):
    length = len(list)
    for x in range(length):
        for y in range(x+1, length):
            if list[x] + list[y] == target:
                return [x, y]
    return
print(twoSum([0,2,1,3,4], 5))
print(twoSum([2,3,7,10,9], 11))


# optimized version
def twoSum(list, target):
    bag = {}  # to store element:index like 3 : 0, 5 : 1 ... from [3,5,1...]
    for i, x in enumerate(list):  # i am getting i = index, x = value
        diff = target - x  # let's say 4 = 9 - 5
        if diff in bag:  # if 4 is in my bag
            return [bag[diff], i]  # i am returning index from my bag, and the other index
        bag[x] = i  # else I am assigning key:value to my bag
print(twoSum([0,2,1,3,4], 5))
print(twoSum([2,3,7,10,9], 11))