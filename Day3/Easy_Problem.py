
#Check whether a number is positive or negative.
num=float(input("Enter a number: "))
if(num>0):
    print(f"Number is positive: {num}")
else:
    print(f"Number is negative: {num}")
    
#Check whether a number is even or odd.
num=float(input("Enter a number: "))

if(num%2==0):   
    print(f"Number is even: {num}")
else:
    print(f"Number is odd: {num}")

#Find the greater of two numbers.
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if(num_1>num_2):
    print(f"{num_1} is greater than {num_2}")
elif(num_1==num_2):
    print(f"Both are equale {num_1} = {num_2}")
else:
    print(f"{num_2} is greater than {num_1}")

#Find the largest of three numbers.
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
num_3=int(input("Enter third number: "))

if(num_1>=num_2 and num_1>=num_3):
    print(f"{num_1} is greater than {num_2} and {num_3}")
elif(num_2>=num_1 and num_2>=num_3):
    print(f"{num_2} is greater than {num_1} and {num_3}")
else:
    print(f"{num_3} is greater than {num_1} and {num_2}")

#Check whether a person is eligible to vote.
age=int(input("Enter your age: "))

if(age>=18):
    print("Your are eligilbe for vote:",age)
elif(age<=0):
    print("This is invalid age")
else:
    print("Sorry your are not eligible")