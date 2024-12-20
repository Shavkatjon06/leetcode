def solution(array, target):
    head = 0
    tail = len(array) - 1
    x = -1  # to keep the index of the smallest element greater than target
    while head <= tail:
        mid = (head + tail) // 2
        if array[mid] > target:
            tail = mid - 1
            x = mid  # current index as a potential answer
        else:
            head = mid + 1
    if array[x] > target:
        return array[x]
    else:
        return array[0]


result = solution(['c', 'f', 'j'], 'c')
print(result)

result = solution(['c', 'f', 'j'], 'a')
print(result)

result = solution([10, 20, 30], 35)
print(result)
