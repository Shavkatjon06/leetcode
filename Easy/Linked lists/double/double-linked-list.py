# insert at the beginning
# insert at a specific position
# append

# delete the first element
# delete a specific element
# delete the last element

# display forward
# display backward

# length

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insertPosition(self, position, data):
        new_node = Node(data)
        if position == 1:
            self.insertBeginning(data)
            return
        current = self.head
        for i in range(1, position-1):
            if current is None:
                print("Position is out of bounds.")
                return
            current = current.next
        if current is None:
            print("Position is out of bounds.")
            return
        new_node.prev = current
        new_node.next = current.next
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def deleteBeginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteSpecific(self, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data:
            self.deleteBeginning()
            return
        current = self.head
        while current:
            if current.data == data:  # 1 -> 2 -> 3, you wanna delete 2
                if current.next:  # if 2.next exists
                    current.next.prev = current.prev  # 2.next.prev means 3.prev = 2.prev (1)
                if current.prev:  # if 2.prev exists, which is 1 in this case
                    current.prev.next = current.next # 2.prev.next, 1.next, = 2.next, 3
                return
            current = current.next
        print("Element not found.")

    def displayForward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.next

    def displayBackward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            if current.prev:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.prev

    def length(self):
        if self.head is None:
            print("List is empty")
            return
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print("Length:", count)
        return


dll = DoubleLinkedList()

dll.insertBeginning(1)
dll.displayForward()  # 1

dll.insertPosition(1, 0)
dll.displayForward()  # 0 -> 1
dll.insertPosition(3, 2)
dll.displayForward()  # 0 -> 1 -> 2

dll.append(3)  # 0 -> 1 -> 2 -> 3
dll.append(4)  # 0 -> 1 -> 2 -> 3 -> 4
dll.displayForward()

dll.displayBackward()  # 4 -> 3 -> 2 -> 1 -> 0

dll.deleteBeginning()
dll.displayForward()  # 1 -> 2 -> 3 -> 4

dll.deleteSpecific(10)  # Element not found in 1 -> 2 -> 3 -> 4

dll.deleteSpecific(2)
dll.displayForward()  # 1 -> 3 -> 4

dll.length()  # Length: 3
