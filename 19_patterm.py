def Triangle_pattern(n):
    for i in range(n+1):
        print(" " * (n-i), end="")
        print("*" * (2*i-1))
        print("\n")
n = int(input("enter the no: "))
a= Triangle_pattern(n)
print(a)
