# c = 5*(f-32)/9
# f = 9*(c+32)/5

def f_c(f):
    return (5*(f-32)/9)
f = int(input("enter the no:"))
c = f_c(f)
print(f"{round(c,2)}")
     10