def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

if __name__ == "__main__":
    arr = [12, 4, 5, 6, 7, 3, 1, 15, 8, 9, 2, 10]
    n = len(arr)
    print("OUTPUT")
    print("Original array: ", end="")
    for num in arr:
        print(num, end=" ")
    print()

    quicksort(arr, 0, n - 1)

    print("Sorted array: ", end="")
    for num in arr:
        print(num, end=" ")
    print()
