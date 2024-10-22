def sqrt(x):
    if x < 0:  # It's not valid to find the square root of a negative number, so return False.
        return False
    head = 0  # Start of the search range.
    tail = x  # End of the search range.
    result = 0  # Variable to store the closest integer square root when an exact one isn't found.
    while head <= tail:
        mid = (head + tail) // 2  # Find the mid
        if mid ** 2 > x:  # If mid squared is greater than x, tail = mid - 1.
            tail = mid - 1
        elif mid ** 2 < x:  # If mid squared is less than x, head = mid + 1.
            head = mid + 1
            result = mid  # current mid as a potential answer.
        else:  # If mid squared equals x, mid is the exact square root.
            return mid
    return result  # If no exact square root was found, return the closest integer result.


print(sqrt(16))
print(sqrt(-4))
print(sqrt(8))
