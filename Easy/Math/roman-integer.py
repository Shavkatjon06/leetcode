def romanToInt(s: str) -> int:
    result = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)):
        if i+1 < len(s) and romans[s[i]] < romans[s[i+1]]:  # compare if the current roman is smaller than the next
            result -= romans[s[i]]  # if above condition is true, then we have to subtract that particular roman
        else:
            result += romans[s[i]]  # else keep adding
    return result
print(romanToInt("III"))
print(romanToInt("MCMXCIV"))
print(romanToInt("XXVII"))