def bubble_sort(arr):
    low = 0
    high = len(arr) 

    for i in range(low, high):
        for j in range(i,high):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [4, 3, 6, 2, 1]
a = bubble_sort(arr)
print(a)