#  string approach
def isPalindrome1(x: int) -> bool:
    if x < 0: return False
    new = str(x)
    if new == new[::-1]:
        return True
    return False


print(isPalindrome1(121))
print(isPalindrome1(3901))
print(isPalindrome1(556655))


#  left-right approach
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False  # if x is negative (-1221), it won't be a palindrome
    division = 1
    while x >= 10 * division:  # let's say x is 1221, division is 1000
        division *= 10
    while x:
        right = x % 10  # we are getting rightmost element: 123 % 10 => 3
        left = x // division  # we are getting leftmost element: 1221 // 1000 => 1
        if right != left:
            return False  # if they are not equal, it's not a palindrome
        x = (x % division) // 10  # (x % division) => (1221 % 1000) removing leftmost element: 221
        # (221) // 10 getting rightmost element: 22
        division = division // 100  # as we got rid of 2 digits (left, right), we will get rid of two 0: 1000 => 10
    return True


print(isPalindrome(12321))  # 12321 => 1 = 1, 2 = 2, 3
print(isPalindrome(1234))  # 1234 => 1 != 4: return False
print(isPalindrome(3553))  # 3553 => 3 = 3, 5 = 5
