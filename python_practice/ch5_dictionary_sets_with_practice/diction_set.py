d1= {}  # this is empty dictionary 

e = set() 
   # this is empty set 

d2 = {
     "name" : "Ali" , 
     "age" : 83 , 
     "city" : "lahore"

}   
print(type(d1))
print(type(e))
print(type(d2))


s1 = {1 ,3 , 5 , 7 , 7 ,9 ,3, 7 ,9, }
s2= {2 ,4 , 6 , 8,10 }

print(s1)
# this will include 7 only one time

s3 = s1.union(s2)
print(s3) 
 
s4 = s1.intersection(s2)
print(s4) 
s4.add(11) 
print(s4) 
s4.clear()
print(s4) 


sample_set = {2 , 93 , "Ali" , 94 , 41 , 93,  4 }
# sample_set.remove(44)
sample_set.discard(44)
sample_set.discard(93)
print(sample_set)

words ={
    "saib": "apple" ,
    "kela" :"banana" ,
    "amrood":"Avacado"

}
# word = input("enter you word ")

# print(words[word])


dict1 = {}

name1 = input("Enter you friend name")
lang1 = input("Enter the favourite language name")
dict1.update({name1:lang1})
name2 = input("Enter you friend name")
lang2 = input("Enter the favourite language name")
dict1.update({name2:lang2})
name3 = input("Enter you friend name")
lang3 = input("Enter the favourite language name")

dict1.update({name3:lang3})
name4 = input("Enter you friend name")
lang4 = input("Enter the favourite language name")
 
dict1.update({name4:lang4})
print(dict1)