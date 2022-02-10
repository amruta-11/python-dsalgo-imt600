
def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        
    # Write a merge function that will take the left, right and middle of the array and create those lists
    # After that compare L[i] and R[i] and fill the array with the lowest
def mSort(start, end, array):
    if start < end:
        mid = start + (end-start)//2
        mSort(start, mid, array)
        mSort(mid+1, end, array)

def comparing(start, mid, end, array):
    left = array[start:mid]
    right = array[mid+1:end]

    i = j = 0

    for k in range(first, end+1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
