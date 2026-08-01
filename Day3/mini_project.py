'''Student Result Management System
Features:

Student Name
Roll Number
Marks of 5 Subjects
Total Marks
Percentage
Grade (using if-elif-else)
Pass/Fail Status'''
#Id
student=input("Enter Student Name: ")
roll_no=input("Enter Sstudent Rollno.: ")

#Marks
s1=float(input("Enter marks of subject 1: "))
s2=float(input("Enter marks of subject 2: "))
s3=float(input("Enter marks of subject 3: "))
s4=float(input("Enter marks of subject 4: "))
s5=float(input("Enter marks of subject 5: "))

total_marks=s1+s2+s3+s4+s5
percentage=(total_marks/5)*100

#Grade
if(total_marks>=90):
    grade="A"
elif(total_marks>=80):
    grade="B"
elif(total_marks>=70):
    grade="C"
elif(total_marks>=60):
    grade="D"
else:
    grade="F"

#Pass/Fail
if(s1 >= 33 and s2 >= 33 and s3 >= 33 and s4 >= 33 and s5 >= 33):
    status="Pass"
else:
    status="Fail"

#Result
print("\n-------------Result--------------")
print(f"Student Name        : {student}")
print(f"Roll No             : {roll_no}")
print(f"Total Marks         : {total_marks}")
print(f"Percentage          : {percentage}")
print(f"Grade               : {grade}")
print(f"Status              : {status}")

