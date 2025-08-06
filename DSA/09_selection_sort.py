def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if arr[j]<arr[min_value]:
                min_value = j
        
        arr[i],arr[min_value] = arr[min_value],arr[i]
    return arr

arr = [4, 2, 5, 6, 2, 1, 8]
a = selection_sort(arr)
print(a)













# error code
"""
def selection_sort(arr):
    low = 0
    high = len(arr) 

    while (low < high):
        mid = (low + high) //2
        if low > mid:
            for i in range[low, mid]:
                for j in range[i+1, mid]:
                    arr[i], arr[j] = arr[j], arr[i]
        
    low = low + 1
    high = high - 1


arr = [4, 2, 5, 6, 2, 1, 8]
a = selection_sort(arr)
print(a)

"""

   
        





