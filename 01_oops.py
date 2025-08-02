class calculator:
    def __init__(self,a):
        self.a = a

    def square(self): 
        result = self.a * self.a
        print(f"the square of the no. is {result}")
    
    def cube(self):
        print(f"the cube of the no. is {self.a * self.a * self.a}")

    def squareroot(self):
        print(f"the squareroot of the no. is {self.a**1/2}") 

    @staticmethod
    def hello():
        print("hello!")
        
a = calculator(int(input("Enter the no:")))
a.hello()
a.square()
a.cube()
a.squareroot()