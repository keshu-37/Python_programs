def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return [i]
    return ("not present")  
target = int(input("Enter: "))
arr = [10, 20, 30, 40, 50, 60]  
print(f"target index is {linear_search(arr, target)}")