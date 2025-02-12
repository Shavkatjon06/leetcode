def selectionSort(arr):
    length = len(arr)  # take length of an array
    for i in range(length-1):  # outer loop to select an element one by one
        smallest_index = i  # save its index assuming it's the smallest element
        for j in range(i+1, length):  # inner loop to compare with the rest of the elements
            if arr[j] < arr[smallest_index]:  # if inner loop element is smaller
                smallest_index = j  # update index
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]  # after inner loop, swap their places
    return arr  # return sorted array


result = selectionSort([64, 12, 25, 11, 9, 4])
print(result)
