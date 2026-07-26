# if (n:=len([38 ,39 , 93 ])) >3:
#     print("length is Greater than 3 ")
# else:
#     print("length is smaller or equal to 3")



# age = int(input("Enter your age: "))

# match age:
#     case a if a < 13:
#         print("Child")
#     case a if 13 <= a < 20:
#         print("Teenager")
#     case a if 20 <= a < 60:
#         print("Adult")
#     case _:
#         print("Senior")


try:
    x = 5 / 0
except Exception as e:
    print("Error occurred:", e)
