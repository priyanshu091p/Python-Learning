# Convert seconds into hours, minutes and seconds
seconds=int(input("Enter total seconds: "))

hours=seconds//3600
remaining_seconds=seconds%3600

minutes=remaining_seconds//60
left_seconds=remaining_seconds%60

print("Hours=",hours)
print("Minutes=",minutes)
print("Seconds=",left_seconds)

#Convert salary after a 15% bonus
salary=int(input("Enter your monthly salary: "))

bonus=salary*15/100
bonus_salary=bonus+salary

print("This is your salary:",salary)
print("And this after got 15% bonus:",bonus_salary)

#Convert rupees into dollars(fixed rate)
rupees=float(input("Enter amount in rupees: "))

dollars = rupees / 85

print(f"Rupees: {rupees:.2f}")
print(f"Dollars: {dollars:.2f}")

#Convert kilometers to meters and centimeters
kilometers=float(input("Enter total distance in kilometers: "))

meters=kilometers*1000
centimeters=kilometers*100000

print("Meters:",meters)
print("centimeters:",centimeters)

#Make a basic calculator using operators (without if)
a=int(input("Enter a number: "))
op=input("Enter operator(+,-,*,/,%,**)")
b=int(input("Enter a number: "))

result={
    "+":    a+b,
    "-":    a-b,
    "*":    a*b,
    "/":    a/b,
    "%":    a%b,
    "**":   a**b,       #power
}
print(f"Result: {result[op]}")


