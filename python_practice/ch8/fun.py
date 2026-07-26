def greet(name  , rollno = 98):
    print("hello" , name , rollno)
    return  


def average(x , y , z):
    average = (x +y+z)/3
    return average

def average2(a , b=9):
    avg2 = a +b/2
    return avg2


greet("Ali" , 8) 

greet("Shafay")

avg = average(98 ,93 ,3939)
print(avg)

print(average2(1))


def factorial(n):
    if (n==0 or n==1):
        return 1 
    return n * factorial(n-1)

num= int(input("Enter the number for  which you find the factorial"))

print(f"The factorial of the provided number is {factorial(num)}")
