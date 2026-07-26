# class Programmer :
#     company = 'Google'
#     def __init__(self , name , salary , pin):
#         self.name = name 
#         self.salary = salary 
#         self.pin = pin 

# p= Programmer("Ali" , 293393 , 339 )
# print(p.name)


class Calculator :
    def __init__(self , n):
        self.n = n 
    
    def square(self):
        print(f"The square is {self.n* self.n}")
    def cube(self):
        print(f"The cube is {self.n* self.n*self.n}")
    def root(self):
        print(f"The square root is {self.n**(1/2)}")

num = int(input("Enter the number for which you want to make calculations"))
choice = int(input("Make your choice : 1= square , 2 = cube , 3 = square root "))
a= Calculator(num)
if (choice ==1 ):
    a.square()
elif(choice ==2):
    a.cube()
elif(choice==3):
    a.root()

else :
    print("Enter only 1 , 2 , or 3")
