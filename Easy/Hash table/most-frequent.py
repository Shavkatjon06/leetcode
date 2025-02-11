# most frequent element in an array

def mostFrequent(arr):
    bag = {}
    for i in arr:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    result = -1
    largest = 0
    for key, value in bag.items():
        if value > largest:
            result = key
            largest = value
    return result


print(mostFrequent([1, 2, 3, 1, 4, 1]))
