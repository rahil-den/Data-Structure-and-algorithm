def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr
            
            
       
    


if  __name__ == '__main__':
    arr = [9,14,8,6,5,36,24]
    print(insertion_sort(arr))