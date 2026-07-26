# class TwoDvector():
#     def __init__(self , i , j):
#         self.i = i 
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self, i, j , k):
#         super().__init__(i, j)
#         self.k = k 

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j +{self.k}k")

# a = TwoDvector(3,59)
# a.show()
# b= ThreeDvector(3737,58, 94)
# b.show()

# class Employee:
#     salary = 234 
#     increment = 39


#     @property 
#     def salaryAfterIncrement(self):
#         return(self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment= ((salary/self.salary)-1)*100


# e = Employee()
# e.salaryAfterIncrement = 393
# print(e.increment)






class Complex:
    def __init__(self , r , i):
        self.r = r 
        self.i = i 

    def __add__(self , c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __str__(self):
          return f"{self.r} + {self.i}i"
    
c1 = Complex(13, 93)
c2 = Complex(38 ,39)

print(f'The sum is of two complex numbers is  {c1 + c2}' )