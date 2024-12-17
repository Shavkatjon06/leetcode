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
        return self.head

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


list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(5)

list2 = LinkedList()
list2.append(3)
list2.append(4)
list2.append(7)
list2.append(10)


def merge(lst1, lst2):
    dummy = Node(0)  # a node to act as a starting point of merged list
    current = dummy  # the last node in merged list
    node1 = lst1.head  # start from heads
    node2 = lst2.head
    while node1 and node2:  # continue till the end of one of the lists
        if node1.data < node2.data:  # if node1 is smaller
            current.next = node1  # append node1 to merged list
            node1 = node1.next  # move to the next node in lst1
        else:
            current.next = node2  # else add node2 from lst2
            node2 = node2.next  # move to the next node in lst2
        current = current.next

    current.next = node1 if node1 else node2  # remaining nodes in lst1 or lst2

    merged = dummy.next  # 'dummy.next' points to the first node of the merged list
    while merged:
        print(merged.data, end=" ")
        merged = merged.next
    print()


merge(list1, list2)
