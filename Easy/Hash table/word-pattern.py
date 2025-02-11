def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    bag = {}
    used_words = set()
    for x, y in zip(pattern, words):
        if x in bag:
            if bag[x] != y:
                return False
        else:
            if y in used_words:
                return False
            else:
                bag[x] = y
                used_words.add(y)
    return True


x = "dog cat cat dog"
print(wordPattern("abba", x))

x = "dog cat cat dog"
print(wordPattern("aaaa", x))

x = "dog cat cat dog"
print(wordPattern("aaaa", x))
