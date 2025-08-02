def greater(a,b,c):
    if ((a > b) and (a>c)):
        print("greater no is:",a)
    elif ((b>a) and (b>c)):
        print("greater no is:",b)
    else:
        print("greater no is:",c)
a = int(input("enter the no:"))
b = int(input("enter the no:"))
c = int(input("enter the no:"))
print(greater(a,b,c))
