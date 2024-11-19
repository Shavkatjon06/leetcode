def removeChars(word1, word2):
    stack = ""
    for i in word1:
        if i not in word2:
            stack += i
    print(stack)
    return

removeChars("computer", "cat")


def removeChars2(word1, word2):
    for i in word2:
        if i in word1:
            word1 = word1.replace(i, "")
    print(word1)
    return

removeChars2("codelabs.uz", 'bus')