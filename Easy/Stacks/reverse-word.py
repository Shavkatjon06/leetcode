from stack import Stack

def reverseWord(word):
    stack = Stack()  # create a new stack: []
    for i in word:  # loop through each character
        stack.push(i)  # append it to the stack
    reverse = ""
    while not stack.isEmpty():  # while our stack have elements  ['h', 'e', 'l', 'l', 'o']
        reverse += stack.pop()  # 'o' -> 'l' -> .... olleh

    print(f"Original: {word}\n"  #
          f"Reversed: {reverse}")

reverseWord("hello")  # "hello" -> "olleh"
