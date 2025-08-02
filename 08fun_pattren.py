def star(n):
    if n == 0:
        return 
    else:
        print("*" * n)
        return star(n-1)
    
n = int(input("k:"))
print(star(n))


            
            