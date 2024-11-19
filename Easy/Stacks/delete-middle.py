from stack import Stack

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(7)
stack.push(9)
stack.push(1)
stack.display()

def deleteMiddle(arr):  # 2,3,7,9,1
    temp = []
    length = len(arr) // 2  # get the middle  len(arr) => 5 // 2 = 2
    while length > 0:  # until we reach the middle
        temp.append(arr.pop())  # we pop items from the end of the arr and append them to temp => 1, 9
        length -= 1  # decrement the length
    arr.pop()  # remove the middle item 7. now we have [2,3]
    while temp:  # while we have items => 1, 9
        arr.append(temp.pop())  # [2,3].append(temp.pop()) => [2,3,9], [2,3,9,1]
    print(arr)


deleteMiddle(stack.stack)
