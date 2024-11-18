# LIFO(Last In First Out) or FILO(First In Last Out)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(7)
stack.display()  # [2, 3, 5, 7]

print(stack.size())  # 4

print(stack.isEmpty())  # False

print(stack.top())  # 7

print(stack.pop())  # 7
stack.display()  # [2, 3, 5]
