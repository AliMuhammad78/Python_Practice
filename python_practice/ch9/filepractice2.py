# def generateTable(n):
#     table = "" 
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)



# for i in range(2,21):
#     generateTable(i)


# word = "Donkey"

# with open("poem.txt" ,"r") as f:
#     content = f.read()

# contentNew= content.replace(word , "######")

# with open("poem.txt" ,"w") as g :
#     g.write(contentNew)


# words = ["stars" , "night" ,"shine"] 

# with open("poem.txt" ,"r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace( word, "#" * len(word))

# with open("poem.txt" ,"w") as g :
#     g.write(content)



with open("poem.txt") as f :
    # content = f.read()
    contentLines = f.readlines()
    

# if("python" in content):
#     print("python is present")
lineNumber= 1
for line in contentLines:
    if("python" in line):
        print(f"Yes python is present at line{lineNumber}")
        break
    lineNumber += 1 
else:
    print("python is not present")


 
