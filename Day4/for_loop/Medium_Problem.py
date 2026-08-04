# Find the sum of first n natural numbers.
n=int(input("Entere a number: "))
sum=0

for i in range(1,n+1):
    sum=sum+i
    print(f"{i} + {sum} ={sum}")

print(f"Sum : {sum}")

# Find the factorial of a number.
num=int(input("Enter a number: "))
fact=1

for i in range(1,num+1):
    fact=fact*i
print(f"Factorial of {num} is: {fact}")

# Count digits in a number.
num=int(input("Enter a number: "))
count=0

for i in range(num+1):
    if(num==0):
       break
    num = num // 10
    count = count + 1

print(f"Total digits: {count}")

# Reverse a number.
num=int(input("Enter a number: "))
reverse=0

for i in range(num+1):
    if(num==0):
        break
    digit = num % 10                    #to find last digit
    reverse = reverse * 10 + digit      #create reverse number
    num = num // 10                     #remove the last digit

print("Reverse =", reverse)

# Find the sum of digits of a number.
num=int(input("Enter a number: "))
sum=0

for i in range(1,num+1):
    if(num==0):
     break
    digit = num % 10                 
    sum=sum+digit  
    num = num // 10                     
    
print("Sum of digits =",sum)

