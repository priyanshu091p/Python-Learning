#Cal. Area of Circle
r=int(input("Enter radius of circle: "))
area_circle=3.14*r*r
print("the area of circle is:",area_circle)'''

#conver kilometers to miles
kilometers=float(input("Enter distance in kilometers:"))
miles=kilometers*0.621371
print("Distance in miles is =",miles)

#Convert minutes into hours and minutes
minutes=int(input("Enter minutes: "))
hours=minutes//60
reaining_minutes=minutes%60
print("Hours =",hours)                              
print("Minutes =",reaining_minutes)

#Gram into Kilogram
gram=int(input("Enter total gram: "))
kilogram=gram//1000
remaining_gram=gram%1000
print("Kilogram=",kilogram)
print("Gram=",remaining_gram)

#days into Months, weeks and days

#cal. marks percentage and total
# days=int(input("enter total days: "))
months=days//30
remaining_days=days%30

week=remaining_days//7
days_left=remaining_days%7
print("Months=",months)
print("Weeks=",week)
print("Days=",days_left)

#cal. marks percentage and total
'''English_marks=int(input("Enter Given Marks in English: "))
Hindi_marks=int(input("Enter Given Marks in Hindi: "))
Mathematics_marks=int(input("Enter Given Marks Mathematics: "))
Science_marks=int(input("Enter Given Marks Science: "))
Computer_marks=int(input("Enter Given Marks Computer: "))

total=English_marks+Mathematics_marks+Hindi_marks+Science_marks+Computer_marks
percentage=(total/600)*100

print("Grand total obtained a student=",total)
print("Marks in percentage=",percentage)'''

 #Buila simple calculator without using if statements
num1=int(input("Enter a number: "))
op=input("Enter operator (+,-,*,/)")
num2=int(input("Enter a number: "))

result={
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2,
}
print("Result =",result[op])