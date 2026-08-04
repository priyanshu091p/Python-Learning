# Print numbers from 1 to 10 using while.
i=1
while(11>i):
    print(i)
    i+=1
# Print numbers from 10 to 1.
i=10
while(i>0):
    print(i)
    i-=1
# Print even numbers from 1 to 50.
i=1
while(i<=50):
    if(i%2==0):
        print(i)
    i+=1

# Print odd numbers from 1 to 50.
i=1
while(i<=50):
    if(i%2!=0):
        print(i)
    i+=1

# Print the multiplication table of a number.
a=int(input("Enter a number "))
i=1
print(f"Table of {a}")

while(i<=10):
    print(f"{a} X {i} = {a*i}")
    i+=1