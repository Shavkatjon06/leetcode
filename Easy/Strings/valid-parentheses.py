def isValid(s: str) -> bool:
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in brackets.values():  # let's say from "()", "(" is in values ")": "("
            stack.append(i)  # we will add "(" to our stack
        elif i in brackets.keys():  # next, ")" is our key from ")": "("
            if not stack or stack.pop() != brackets[i]:  #  stack.pop() will get "(" and brackets[i] will get brackets[")"] => "("
                # so if "(" from our stack != "(" from our brackets[")"]
                return False  # it's False
    return True if not stack else False  # if our stack is empty, then all brackets are matched, else there's still some left, False

print(isValid("()[]"))
print(isValid("([{}])"))
print(isValid("}(){}"))
print(isValid("(){}}"))