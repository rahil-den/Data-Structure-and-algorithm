
# This Readme contains all about sorting algorithms  


### I have gained this knowledge from different resources like Striver A2Z Sheet and GeeksforGeeks.  
---

## What is Sorting?

> Sorting is a term used in Data Structures for arranging arrays in either ascending or descending order.  
> There are various ways one can sort an array such as:
> - Selection Sort  
> - Bubble Sort  
> - Insertion Sort  
> - Merge Sort  
> - Quick Sort  
> - Heap Sort  
> - And many more...

---

## Progress Tracker

| Sr. No | Sorting Algorithm |
|--------|-------------------|
| 1.     | [Selection Sort](#1-selection-sort) |
| 2.     | [Bubble Sort](#2-bubble-sort) |
| 3.     | [Insertion Sort](#3-insertion-sort) |

---

## 1. Selection Sort

### What is Selection Sort?

> Selection Sort is a sorting algorithm where we repeatedly pick the **minimum** element from the unsorted part of the array and place it at the correct position by swapping it with the current element.

Let’s take an example:  
`ARR = [21, 23, 42, 12, 9]`

In the first pass, the minimum value is `9`, so we swap it with the first element (`21`).  
Now the array becomes: `[9, 23, 42, 12, 21]`  
This process continues until the entire array is sorted.

---

### Algorithm for Selection Sort

1. First, declare the array as `arr` and initialize it with random values.  
2. Run the first `for` loop from `i = 0` to `n - 1`.  
   This loop will go through each element of the array.  
3. At each iteration, assume the current index `i` is the `minimum_element`.  
4. Now run another `for` loop from `j = i + 1` to `n`.  
   In this loop, check if `arr[j] < arr[minimum_element]`.  
   If true, update `minimum_element = j`.  
5. After the inner loop ends, **swap** `arr[i]` with `arr[minimum_element]`.  
6. Repeat steps 3 to 5 for every element until the array is sorted.

---

### Python Code Example

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [21, 23, 42, 12, 9]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
````

---

### Time and Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n²)           |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |

| Space Complexity |
| ---------------- |
| O(1)             |

---

## 2. Bubble Sort

### What is Bubble Sort?

> Bubble Sort is a sorting algorithm where we **repeatedly compare adjacent elements**, and if they are in the wrong order, we **swap them**.
> After each full pass, the **largest element bubbles up to its correct position** at the end of the array.

Let’s take an example:
`ARR = [21, 23, 42, 12, 9]`

* First pass:

  * Compare 21 and 23 → OK
  * Compare 23 and 42 → OK
  * Compare 42 and 12 → swap → `[21, 23, 12, 42, 9]`
  * Compare 42 and 9 → swap → `[21, 23, 12, 9, 42]`
    → Now 42 is at the correct position (end of the array)

* The process repeats until the array is sorted.

---

### Algorithm for Bubble Sort

1. First, declare the array as `arr` and initialize it with random values.
2. Run the outer loop from `i = 0` to `n - 1`.
   This loop counts how many passes we’ve made.
3. Inside that, run the inner loop from `j = 0` to `n - i - 1`.
4. At each step, compare `arr[j]` with `arr[j + 1]`.
5. If `arr[j] > arr[j + 1]`, **swap** them.
6. After each outer loop, the largest unsorted element will be at the end.
7. Repeat until the array is sorted.

---

### Python Code Example

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
arr = [21, 23, 42, 12, 9]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
```

---

### Output

```
Sorted array: [9, 12, 21, 23, 42]
```

---

### Time and Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n)            |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |

| Space Complexity |
| ---------------- |
| O(1)             |

---


Sure! Here's the **Insertion Sort** explanation following the **same theme and format** as your Bubble Sort section:

---

## 3. Insertion Sort

### What is Insertion Sort?

> Insertion Sort is a sorting algorithm where we **build the sorted array one item at a time**.
> At each step, we **take the next element and insert it into its correct position** in the already sorted part of the array.

Let’s take an example:
`ARR = [21, 23, 42, 12, 9]`

* First element (21) is considered sorted.
* Next, compare 23 with 21 → OK → `[21, 23, 42, 12, 9]`
* Compare 42 with 23 → OK → `[21, 23, 42, 12, 9]`
* Compare 12 with 42 → swap
  Compare 12 with 23 → swap
  Compare 12 with 21 → swap → `[12, 21, 23, 42, 9]`
* Compare 9 with 42 → swap
  Compare 9 with 23 → swap
  Compare 9 with 21 → swap
  Compare 9 with 12 → swap → `[9, 12, 21, 23, 42]`

→ Now the array is sorted.

---

### Algorithm for Insertion Sort

1. First, declare the array as `arr` and initialize it with values.
2. Start the loop from `i = 1` to `n - 1`.
   (Assume the first element is already sorted)
3. Store the current value in `key = arr[i]`.
4. Compare `key` with the elements before it (from `j = i - 1` to `0`).
5. If `arr[j] > key`, shift `arr[j]` one position to the right.
6. Place `key` in its correct position.
7. Repeat until the array is sorted.

---

### Python Code Example

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr

# Example usage:
arr = [21, 23, 42, 12, 9]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
```

---

### Output

```
Sorted array: [9, 12, 21, 23, 42]
```

---

### Time and Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n)            |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |

| Space Complexity |
| ---------------- |
| O(1)             |

---






### This page was created by [Rahil](https://github.com/rahil-den)


