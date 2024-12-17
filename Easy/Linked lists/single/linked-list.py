# append
# insert at the beginning
# insert after a particular node
# delete from the beginning
# delete a specific node
# delete from the end
# find
# display
# length

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

    def insertBeginning(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAfterNode(self, targetNode, item):
        if self.head is None:
            return "List is empty!"
        current = self.head
        while current:
            if current.data == targetNode:
                break
            current = current.next
        if current is None:
            return "Target nod is not found!"
        new_node = Node(item)
        new_node.next = current.next
        current.next = new_node
        return self.head

    def deleteBeginning(self):
        if self.head is None:
            return "List is empty!"
        self.head = self.head.next
        return self.head

    def deleteSpecific(self, item):
        if self.head is None:
            return "List is empty!"
        if self.head.data == item:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                return
            current = current.next
        return f"Item {item} is not found!"

    def deleteEnd(self):
        if self.head is None:
            return "List is empty!"
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        return

    def find(self, item):
        if self.head is None:
            return "List is empty!"
        current = self.head
        while current:
            if current.data == item:
                return f"{item} node exists in the list."
            current = current.next
        return f"Item {item} is not found"

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

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return f"Length: {count}"


list = LinkedList()
list.append(2)
list.append(4)
list.append(5)
list.append(9)
list.display()

print(list.length())

list.insertBeginning(0)
list.display()

list.deleteSpecific(5)
list.display()
