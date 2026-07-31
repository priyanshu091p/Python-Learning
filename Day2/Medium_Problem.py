num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))

square1=num1**2     #square of number
cube1=num1**3       #cube of number
square2=num2**2
cube2=num2**3

print(f"Square of {num1} = {square1}")
print(f"Cube of {num1} = {cube1}")
print(f"Square of {num2} = {square2}")
print(f"Cube of {num2} = {cube2}")

#Calculate Average of three numbers
average=(num1 + num2 + num3) / 3
print("Average of three numbers =",average)

#Calculate Simple Interest
p=float(input("Enter Principle: "))
r=float(input("Enter Rate: "))
t=float(input("Enter Time : "))

si=(p * r * t) / 100

print("Simple Interest is :",si)

#Calculate the area of triangle
b=int(input("Enter base of tringle: "))
h=int(input("Enter height of triangle: "))

area = b * h
print("The area of triangle is =",area)