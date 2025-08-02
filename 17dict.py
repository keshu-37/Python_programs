Dict = {"love":"pyar","bitch":"kutiya","mango":"aam","man":"adami","women":"orate"} 
print( '''ENTER THE WORD WHICH YOU WANT TO COVERT IN HINDI!
      1.love
      2.bitch
      3.mango
      4.man
      5.women
      
    ''')
a = input("enter:")
b= Dict.get(a)
print("meaning is: ",b )
