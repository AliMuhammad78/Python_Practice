class Employee:
    language = "Urdu"
    salary = 29283
    company = "Google"

    def __init__(self, language=None, salary=None, company=None):
        if language is not None:
            self.language = language
        if salary is not None:
            self.salary = salary
        if company is not None:
            self.company = company

   
    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}, Company is {self.company}")
    @staticmethod
    def greet():
        print("Hello")
    # def getInfo():
    #     print(f"The language is {language} , the salary is {salary}")
    # don't do that it will overwrite the first function


Employee.company = "YouTube" 
#  attribute of the class is changed outside the class


e1 = Employee()
print( "salary is "  , e1.salary)
e1.name = "ali"  # name is here the particular object attribute

print(e1.name)

e2 = Employee()
e2.salary= 11111
#: Instance attributes, take preference over class attributes during assignment & 
# retrieval. 
print(e2.salary) 

e1.getInfo()
e2.getInfo()


e3 =Employee("english" , 5000 , "Nestle")
e3.getInfo()
e3.greet()
