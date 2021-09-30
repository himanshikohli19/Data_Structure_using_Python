#Counting Sort

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max(array)+1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, max(array)+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        count[array[i]] -= 1
        output[count[array[i]]] = array[i]
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4,2,2,8,3,0,1,0,10,5,7,8,9,6,3,4]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
