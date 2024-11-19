from stack import Stack

def isValid(x):
    bag = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for i in x:
        if i in bag.values():
            stack.push(i)
        elif i in bag.keys():
            if stack.isEmpty() or stack.pop() != bag[i]:
                return False
    return stack.isEmpty()

print(isValid("[()]"))
print(isValid("{}]"))
