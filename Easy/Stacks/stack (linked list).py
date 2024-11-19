class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        temp = self.head
        self.head = self.head.next
        del temp

    def top(self):
        if not self.isEmpty():
            print(self.head.data)
            return
        else:
            return "Stack is empty!"

    def display(self):
        current = self.head
        while current:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=", ")
            current = current.next


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(9)
stack.display()

stack.pop()
stack.display()

stack.top()