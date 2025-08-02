
Fruits = []
#for i in range(1):
for j in range(5):
    #j = j+1 
    A = input(f"Enter name{j+1}:")
    Fruits.append(A)
print(Fruits)

marks = []
L = input("marks 1:")
marks.append(L)
L1 = input("marks 2:")
marks.append(L1)
L2 = input("marks 3:")
marks.append(L2)
marks.sort(reverse = False)
sorted_marks = sorted(marks)
print("Marks are:", sorted_marks)

a = (7,0,8,0,0,9)
print("No of zeros: ",a.count(0)) 