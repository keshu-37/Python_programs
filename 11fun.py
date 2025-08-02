def rem(l , word):
    n=[]
    for item in l:
        if (item == word):
            n.append(word)
    return n
l = ["harry","Rohan","shubham","an"]
print(rem(l,"an"))
