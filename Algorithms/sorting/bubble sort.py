my_array = [8, 22, 7, 9, 31, 5, 13]
length = len(my_array) - 1

for i in range(length):
    for j in range(length - i):
        # traverse the array from 0 to length-i
        # swap if the found element is greater
        # than the next
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]


print("Sorted array:", my_array)
