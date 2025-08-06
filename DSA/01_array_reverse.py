
"""
arr = [1,2,3,4,5]
a = arr.reverse()
print(arr)
"""

def rev_arr(arr):
    start = 0 
    end = len(arr) -1

    while (start < end ):
        arr[start],arr[end] = arr[end],arr[start]

        start = start + 1
        end = end - 1
    return arr
arr = [1,2,3,4,5]
print(f"reverse arry is {rev_arr(arr)}")
