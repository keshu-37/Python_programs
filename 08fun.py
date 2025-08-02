def ninja(n):
    if n==0:
        return
    print("coding ninja",end=" ")
    return ninja(n-1)    
ninja(3)