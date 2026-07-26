def greatest( a ,b , c):
    if(a>b and a>c ) :
        return a
    elif(b>a and b>c ) :
        return b
    else:
        return c 

maxi = greatest(83 , 933 , 932)
print("The largest number is " , maxi)


# sum of all natural numbers 

# def sum(n):
#     if (n==0):
#         print("please enter number greater than zero")
#         return 0 
#     if (n==1 ):
#         return 1 
#     return n + sum(n-1)

# sumnum = int(input("enter the number till where you want to find the sum"))
# print("The total sum is " , sum(sumnum))





def rem(l1 , word):
    n= []
    for item in l1 : 
        if item != word : 
            n.append(item.strip(word)) 
    return n  


list1 = ["Ali" , "Muhammad" , "ghalib" , "ghaib"]

print("After removing gha from list " , rem(list1 , "gha" ))


