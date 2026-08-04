# Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

# Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

# Print even numbers from 1 to 100.
for i in range(2,101,2):
    print(i)

# Print odd numbers from 1 to 100.
for i in range(1,101,2):
     print(i)

# Print the multiplication table of a number.#
a=int(input("Enter a number "))

for i in range(1,11):
    print(f"{a} X {i} =",a*i)

