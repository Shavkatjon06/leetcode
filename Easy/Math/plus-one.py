def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):  # we loop through from the last digit
        if digits[i] < 9:  # if it's less than 9, 1234
            digits[i] += 1  # we add 1 to the last element, 1235
            return digits
        digits[i] = 0  # it means it's 9, we make it 0, [9] => [0]
    return [1] + digits  # [1] + [0] => [1,0]


print(plusOne([1,2,3,4]))
print(plusOne([9,9,9]))
print(plusOne([1,9]))