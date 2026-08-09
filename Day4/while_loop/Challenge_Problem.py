# Check whether a number is a palindrome.
a=int(input("Enter a number: "))
i=0
original=a
reverse=0
while(i<a):
    if(a==0):
        break
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
if(reverse==original):
    print(f"{original} is palindrome number")
else:
    print("this is not palindrome")

# Check whether a number is an Armstrong number.
a=int(input("Enter a number: "))
sum=0
original=a
i=0

while(i<a):
    if(a==0):
        break
    digit=a%10
    sum=sum+(digit*digit*digit)
    a=a//10

if(original==sum):
    print(f"{original} is a Armstrong number")
else:
    print("This is not")

# Print the Fibonacci series using while.
t=int(input("Entr total terms: "))
a=0
b=1
count=0

while(count<t):
    print(a,end=" ")

    c=a+b
    a=b
    b=c
    count=count+1

# Print all prime numbers from 1 to n.
n=int(input("Enter a number: "))
num=2

while(num<=n):
    i=2
    prime=True

    while(i<num):
        if num % i == 0:
            prime = False
            break
        i = i + 1

    if(prime):
        print(num)

    num = num + 1

# Create a menu that keeps running until the user chooses Exit.
while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice=int(input("Enter your choice: "))

    if(choice==5):
        print("Program Ended")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if(choice==1):
        print("Result =", num1 + num2)

    elif(choice==2):
        print("Result =", num1 - num2)

    elif(choice==3):
        print("Result =", num1 * num2)

    elif(choice==4):
        if num2!=0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero is not possible.")

    else:
        print("Invalid Choice")