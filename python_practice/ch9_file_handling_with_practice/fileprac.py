# f = open("E:\python\codeWithHarry\ch9\poem.txt")
# poem = f.readlines()
# print(poem) 



# print lines using while loop 

# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()
 



# writing
 
# w = open("E:\python\codeWithHarry\ch9\poem2.txt","w")
# st =  """ A silver mist clings softly to the ground, 
#          Before the waking life makes any sound.
#          """
# w.write(st)
# w.close() 


# appending 
# appending_String = " Allah hu akbar 02\n "
# f = open("poem.txt" , "a")
# f.write(appending_String)
# f.close()



# exercise question 1
# f = open("poem.txt" , "r")
# content = f.read()
# if ("twinkle" in content):
#     print("present")
# else:
#     print("not present")
# f.close()


import random

def game():
    print("You are playing the game")
    score = random.randint(1,62)

    with open("hiscore.txt") as f :
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore=0

    print("Your Score is: " , score) 
    if(score>hiscore):
        with open("hiscore.txt" , "w") as f :
            f.write(str(score))
    return score





game()