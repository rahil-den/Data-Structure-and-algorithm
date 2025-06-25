def bubble_sort(arr):
    n = len(arr) # N for the array.
    for i in range(n-1,-1,-1):
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# Sorted array: [12, 21, 23, 42, 9]


if __name__ == '__main__':
    arr = [21, 23, 42, 12, 9]
    bubble_sort = bubble_sort(arr)
    print("Sorted array:", bubble_sort)

   