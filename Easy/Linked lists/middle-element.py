class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            return "List is empty!"
        current = self.head
        while current:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=", ")
            current = current.next

    def getMiddle(self):
        if self.head is None:
            return "List is empty!"
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print("Middle: ", slow.data)


list = LinkedList()
list.append(2)
list.append(3)
list.append(5)
list.append(7)
list.append(9)
list.display()
list.getMiddle()
