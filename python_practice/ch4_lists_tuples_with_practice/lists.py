random_data = [3, 1, 4, 1 , 6, 5, 3, 5 , "Ali " , "kitab", "salam" , False , 3.4] 
print(random_data)
print(type(random_data))
print(len(random_data))
print(random_data[0:5])
print(random_data[9])
random_data[0] = "Salam"
print(random_data)

random_data.append("Dunya")
print(random_data) 

random_data.pop()
print(random_data)

random_data.remove(1)
print(random_data) 

random_data.insert(2, "kya hal hai")
print(random_data)


l1 = [3, 5, 7, 9]
l2 = [2, 4, 6, 8]
l1.extend(l2)
print(l1)
print(l2)
print(l2.reverse())

 


random_data.remove(5)   #remove first occurrence of 5
print(random_data)
print(random_data[0:5])

l1.sort()  
print(l1)
print(l1.reverse())




