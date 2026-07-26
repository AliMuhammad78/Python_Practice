# def myFunction():
#     print("Hello Ali")
# myFunction()
# print(__name__) 


a = 93 
def abb():
    global a
    a = 92
    print(a)


abb()
print(a) 


list_1 = [2 , 9 , 3 , 5 , 7 , 8 , 93 , 929 ,4 , 578]
list_2 = [item for item in list_1 if item > 8]
squaredList = [i*i for i in list_1]
print(list_2)
print(squaredList) 