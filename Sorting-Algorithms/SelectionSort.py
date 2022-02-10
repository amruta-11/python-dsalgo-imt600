numbers = [99,44,100,1,14,85,45,63,74]


def selectionSort(array):
    length = len(array)
    minIndex = 0

    for i in range(0, length):
        minNum = array[i]
        for j in range(i+1, length):
            if array[j] < minNum:
                minNum = array[j]
                minIndex = j
        array[i], array[minIndex] = minNum, array[i]

selectionSort(numbers)
print(numbers)
