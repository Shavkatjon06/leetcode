def anagram(x, y):
    if len(x) != len(y):  # if lengths are different, it can't be anagram
        return False
    bag = {}  # let's create hash table to keep count of each character
    for i in x:
        if i in bag:  # if character in word 'x' is in our bag
            bag[i] += 1  # increment count by 1
        else:
            bag[i] = 1  # else add it by giving count 1
    for i in y:  # let's check the second word
        if i not in bag:  # if character is not in our bag, it's not anagram
            return False
        bag[i] -= 1  # if it's in our bag, decrement count by 1
        if bag[i] < 0:  # if count is less than 0, return False => "cat" and "tact", we have 2 t
            return False
    return True


print(anagram("rat", "car"))
print(anagram("hello", "ollle"))
