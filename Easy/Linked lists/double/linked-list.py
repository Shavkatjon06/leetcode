# insert at the beginning
# insert at a specific position
# insert to the last

# delete beginning
# delete the last

# display forward
# display backward

# length

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def displayForward(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


def displayBackward(tail):
    current = tail
    while current:
        print(current.data, end=" ")
        current = current.prev
    print()


def insertBeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


def insertEnd(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    return head


def insertPosition(head, position, data):
    new_node = Node(data)
    if position == 1:
        new_node.next = head
        if head:
            head.prev = new_node
        head = new_node
        return head
    current = head
    for _ in range(1, position-1):
        if current is None:
            print("Position is out of bounds")
            return head
        current = current.next
    if current is None:
        print("Position is out of bounds")
        return head
    print(current.data)
    new_node.prev = current
    new_node.next = current.next
    current.next = new_node
    if new_node.next:
        new_node.next.prev = new_node
    return head


def deleteBeginning(head):
    if head is None:
        return "List is empty."
    head = head.next
    if head:
        head.prev = None
    return head


def deleteEnding(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    print("Length: ", count)


head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.prev = head
second.next = third
third.prev = second

print("Forward")
displayForward(head)

print("Backward")
displayBackward(third)

length(head)

head = insertBeginning(head, 0)
displayForward(head)

head = insertEnd(head, 5)
displayForward(head)

position = 5
head = insertPosition(head, position, 4)
displayForward(head)


head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
displayForward(head)
head = deleteBeginning(head)
displayForward(head)

head = deleteEnding(head)
displayForward(head)