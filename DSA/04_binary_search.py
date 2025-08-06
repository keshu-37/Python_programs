def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while (first <= last):
        mid = (first + last) // 2

        if arr[mid] == target:
            return mid
        
        elif (target > arr[mid]):
            first = mid + 1

        else:
            last = last - 1
    return -1

arr = [10, 20, 30, 40, 50, 60]
target = 30
print(f"ouput is {binary_search(arr, target)}")
