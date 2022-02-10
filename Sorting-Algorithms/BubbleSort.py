numbers = [99,44,100,1,14,85,45,63,74]

def bubbleSort(array):

    length = len(array)

    for i in range(0, length):
        for j in range(0, length-1):
            if array[j] > array[j+1]:
                # Swapping
                array[j], array[j+1] = array[j+1], array[j]

bubbleSort(numbers)
print(numbers)
