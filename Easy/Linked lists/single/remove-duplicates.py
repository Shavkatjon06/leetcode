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
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def removeDuplicates(self):
        if self.head is None:  # if our head is None
            print("List is empty")
            return
        current = self.head
        while current and current.next:
            if current.data == current.next.data:  # if current value is equal to the next node's value
                current.next = current.next.next  # skip the duplicate
            else:
                current = current.next  # else keep seeing the next node


list = LinkedList()
list.append(1)
list.append(2)
list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.display()
list.removeDuplicates()
list.display()
