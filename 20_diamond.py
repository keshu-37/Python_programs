# only for odd no
def diamond_pattern(length):
    mid = length // 2
    i = 1
    while (i <= mid):   
        print(" " * (mid - i), end= "")
        print("*" * (2*i - 1), end= "")
        print("\n")
        i = i + 1
    i = mid - 1
    while i >= 0:
        print(" " * (mid - i), end= "")
        print("*" * (2*i - 1), end= "")
        print("\n") 
        i = i - 1
length = int(input("Enter Ther Length of The Diamond: "))
a = diamond_pattern(length)
print(a)

