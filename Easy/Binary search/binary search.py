def search(array, target):
    head = 0
    tail = len(array) - 1
    while head < tail:
        mid = (head + tail) // 2
        if array[mid] == target:
            return f"{target} is at {mid} index."
        if array[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return f"{target} is at not found."


binary_search = search([3,7,10,13,18,30,42], 13)
print(binary_search)
