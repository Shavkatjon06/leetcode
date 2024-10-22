def addBinary(a, b):
    sum = int(a, 2) + int(b, 2)  # from binary to decimal and their sum
    binary = ""  # create an empty string for binary result
    if sum == 0:  # if sum is 0
        return "0"
    while sum > 0:
        if sum % 2 == 1:  # let's say 11 % 2 == 1
            binary = '1' + binary  # '1'+''
            sum = sum // 2  # 11 // 2 = 5
        else:
            binary = '0' + binary  # if sum % 2 == 0, then '0' + binary
            sum = sum // 2
    return binary


print(addBinary("1010", "1011"))

# from binary to decimal
# int("1011", 2) => 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8+0+2+1 = 11. So if we convert 11 to
# binary string, it would be "1011"
