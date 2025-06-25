
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum_element = i # Taking the minimum element
        for j in range(i+1,n):
            if arr[j] < arr[minimum_element]:
                minimum_element = j
        arr[i],arr[minimum_element] = arr[minimum_element],arr[i]
    return arr
        


if __name__ == '__main__':
    arr = [21, 23, 42, 12, 9]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
