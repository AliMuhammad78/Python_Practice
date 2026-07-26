for i in range(39):
    if (i==19):
        break 
    print(i)


for i in range(42):
    pass          #pass means ignore this abi k liye ,, mean i will work on this later 

for i in range(10):
    if (i==4):
        continue
    print(i)    


# table of 7 

n= int(input("Enter a number to see the table ")) 

#normal table 

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# reverse table 

for i in range(1,11):
    print(f"{n}X {11-i} = {n*(11-i)}")




# factorial

# facNum = int(input("Enter the number to calculate the factorial ")) 

# product = 1 

# for i in range ( 1 , facNum+1 ):
#     product = product*i 
# print(f"The factorial of {facNum} is {product}")





star_rows  = int(input("Enter the number of rows for stars")) 
for i in range(1 , star_rows+1 ):
    print(" " * (star_rows-i) , end="")
    print("*" * (2*i - 1) , end="")
    print("")
