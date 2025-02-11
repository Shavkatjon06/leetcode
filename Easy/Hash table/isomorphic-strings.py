def isomorphic(x, y):
    bag1, bag2 = {}, {}
    for char1, char2 in zip(x, y):
        if (char1 in bag1 and bag1[char1] != char2) or (char2 in bag2 and bag2[char2] != char1):
            return False
        bag1[char1] = char2
        bag2[char2] = char1
    return True


print(isomorphic('egg', 'add'))
print(isomorphic('foo', 'bar'))
print(isomorphic('paper', 'title'))
print(isomorphic('papee', 'title'))
