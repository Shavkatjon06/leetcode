def strStr(word, part):
    if len(word) < len(part):
        return -1
    length = len(part)
    for i in range(len(word)):
        if word[i:i+length] == part:  # if, let's say, hello[0:0+2] == 'll'
            return i  # then returns i
    return -1  # otherwise -1
print(strStr("hello", "ll"))  # hello[2:4] == 'll', answer = 2