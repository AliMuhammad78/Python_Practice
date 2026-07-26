marks1 = int(input("Enter marks of subject1")) 
marks2 = int(input("Enter marks of subject2")) 
marks3 = int(input("Enter marks of subject3")) 
total_marks = 100 

total_percentage = ((marks1 + marks2 + marks3)/300)*100; 

sub1_percentage = (marks1 /total_marks)*100
sub2_percentage = (marks2 /total_marks)*100
sub3_percentage = (marks3/total_marks)*100

if (sub1_percentage < 33 or sub2_percentage <33 or sub3_percentage<33):
    print("you failed the exam")
elif(total_percentage <40):
    print("You failed the exam")
else:
    print("You passed the exam , congrats with percentage" , total_percentage)



message = "I am in Lahore"
print("am" in message) 
# True