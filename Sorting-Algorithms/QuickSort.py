
nums = [10,5,12,15,7,16,15,-16,18,-10]
# QuickSort Recursive Algorithm
def QuickSort(low, high, array):
    if low < high:
        p = part(low, high, array)
        # print(low, high, p)
        print(array)
        QuickSort(low, p-1, array)
        QuickSort(p+1, high, array)

# Partition Algorithm
def part(low, high, array):
    pivot = array[low]
    pivot_index = low
    i = low
    j = high

    while i < j:
        while i < high and array[i] <= pivot:
            i+=1
        while j > low and array[j] > pivot:
            j-=1
        # Swap
        # print(array[i], array[j])
        if i < j:
            array[i], array[j] = array[j], array[i]

    # print(array[j], array[pivot_index])
    array[j], array[pivot_index] = array[pivot_index], array[j]

    return(j)

QuickSort(0, len(nums)-1, nums)
print(nums)
