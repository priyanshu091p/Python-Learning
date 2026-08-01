#Check whether a year is a leap year.
year=int(input("Enter year: "))

if(year % 400==0 or year %4==0 and year%100==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year"

#Check whether a character is a vowel or consonant.
char=input("Enter any character: ")

if char in "aeiouAEIOU":
    print(f"{char} is vowel")
else:
    print(f"{char} is constant")

#Check whether a student has passed (marks ≥ 33).
marks=float(input("Enter student marks:"))

if(marks>=33):
    print("pass")
else:
    print("Fail")

#Find the greatest of four numbers.
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
num_3=int(input("Enter third number: "))
num_4=int(input("Enter fourth number: "))

if(num_1>=num_2 and num_1>=num_3 and num_1>=num_4):
    print(num_1)
elif(num_2>=num_1 and num_2>=num_3 and num_2>=num_4):
    print(num_2)
elif(num_3>=num_1 and num_3>=num_2 and num_3>=num_4):
    print(num_3)
else:
    print(num_4)
    
#Check whether a number is divisible by both 5 and 11.
num=int(input("Enter a number: "))

if(num%5==0 and num%11==0):
    print(f"{num} is divisible by both 5 and 11")
else:
    print("this is not divisible by both 5 and 11")
