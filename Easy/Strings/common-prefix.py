def longestCommonPrefix1(strs: list[str]) -> str:
    first = strs[0]  # let's take first string element from array
    length = len(first)  # let's take its length too
    for i in strs[1:]:  # loop through the rest elements except first (we already have it above)
        while first != i[0:length]:  # if first and particular i string element is not equal
            length -= 1  # decrement length by one, let's say horse - 5, so length will be 5 - 1 = 4
            if length == 0:  # if length is 0
                return ""  # then we don't have common prefix
            first = first[0:length]  # as we decrement length, our first string element will lose characters, from horse to hors - first[0:4]
    return first
print(longestCommonPrefix1(['horse', 'rose']))
print(longestCommonPrefix1(['flight', 'flower']))


def longestCommonPrefix2(strs: list[str]) -> str:
    result = ""  # let's save our prefixes here
    for i in range(len(strs[0])):  # we will loop through each character in our first string element
        for x in strs:  # and each string element in our list
            if i == len(x) or x[i] != strs[0][i]:  # 1. i checks if index i exceeds the length of the current string.
                                                   # 2. if our character in x (horse - h) is not equal to the 1st character of first element (jack - j)
                return result  # then we don't have common prefix
        result += strs[0][i]  # else we will add found prefix character to our result
    return result
print(longestCommonPrefix2(['flower', 'flight', 'flue']))