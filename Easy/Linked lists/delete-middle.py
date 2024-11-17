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
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return

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

    def deleteMiddle(self):
        if self.head is None:
            return "List is empty!"
        if self.head.next is None:  # let's say we have only 1 element
            self.head = None
            return self.head
        prev = None  # to store the node before middle node
        slow = self.head  # after while loop 'slow' will point to the middle
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next  # node before middle-node will point to middle.next, in this way we omit middle node
        return self.head


list = LinkedList()
list.append(2)
list.append(3)
list.append(5)
list.append(7)
list.append(11)
list.display()  # 2, 3, 5, 7, 11

list.deleteMiddle()
list.display()  # 2, 3, 7, 11
