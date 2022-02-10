numbers = [99,44,100,1,14,85,45,45,-1,-100]

def insertionSort(array):
    length = len(array)
    for i in range(0, length):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j], array[j+1] = array[j+1], array[j]
            j-=1

insertionSort(numbers)
print(numbers)
