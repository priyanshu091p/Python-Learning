#Print this pattern:
'''     *
        **
        ***
        ****
        *****   '''  
'''for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()'''


#Print:
'''     *****
        ****
        ***
        **
        *     
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()

#Print a multiplication table from 1 to 10.
for i in range(1,11):
    print(f"Table of {i}")

    for j in range(1,11):
        print(f"{i} X {j} = {i*j}",)
    print()

#Check whether a number is prime.
a=int(input("Enter a number: "))
count = 0

for i in range(1, a+1):
    if a%i==0:
        count=count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")'''

#Print the Fibonacci series up to n terms.
t=int(input("Enter number of terms: "))
a=0
b=1

for i in range(t):
    print(a,end=" ")

    c=a+b
    a=b
    b=c