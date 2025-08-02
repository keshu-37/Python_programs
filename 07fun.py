def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1)+n 
        
n = int(input("enter the no: "))
print(F"sum of the no are {sum(n)}")