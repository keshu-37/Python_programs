def sum_n(n):
    if n==1:
        return 1
    return sum_n(n-1)+n
n = int(input("k:3"))
print(sum_n(n))



 