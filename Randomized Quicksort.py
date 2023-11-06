import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition_left(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)
    return i

def partition_right(arr, low, high):
    random.seed()
    r = low + random.randint(0, high - low)
    swap(arr, r, high)
    return partition_left(arr, low, high)

def quicksort(arr, low, high):
    if low < high:
        p = partition_right(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    arr = [6, 4, 12, 8, 15, 16]
    n = len(arr)
    print("OUTPUT")
    print("Original array: ")
    print_array(arr)
    quicksort(arr, 0, n - 1)
    print("Sorted array: ")
    print_array(arr)


