#Find the sum of first n natural numbers.
n=int(input("Entere a number: "))
sum=0
i=1

while(i<=n):
    sum=sum+i
    i+=1
print(f"Sum : {sum}")

#Find the factorial of a number.
n=int(input("Entere a number: "))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i+=1
print(f"factorial of {n} is: {fact}")

#Reverse a number.
a=123
i=1
reverse=0

while(i<=a):
    if(a==0):
        break
    digit=a%10
    reverse=reverse*10+digit
    a=a//10

print("Reverse =", reverse)

#Find the sum of digits of a number.

a=int(input("Enter a number "))
sum=0
i=1

while(i<=a):
    digit=a%10
    sum=sum+digit
    a=a//10

print("Sum =",sum)

#Count the digits in a number.
a=int(input("Enter a number "))
count=0

while(a>0):
    digit=a%10
    count=count+1
    a=a//10

print("Count =",count)