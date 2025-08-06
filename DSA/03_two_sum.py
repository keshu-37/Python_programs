def two_sum(arr, target):
    n = len(arr)   
    for i in range(n):
        for j in range (i+1, n):
            if arr[i] + arr[j] == target:
                return [i,j]
            
    return ("not available")

target = int(input("Enter No:"))
arr = [1,2,3,7,10]
print(f"the index of the sum is {two_sum(arr, target)}")