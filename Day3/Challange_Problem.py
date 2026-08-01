#Grade Calculator (A, B, C, D, F)
marks=int(input("Enter marks of student: "))

if(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
else:
    print("F")
    
#Electricity Bill Calculator (using slabs)
units=float(input("Enter total units: "))
if(units<=100):
    bill=units*5
elif(units<=200):
    bill=units*7
else:
    bill=units*10
print("Electricity Bill = ₹", bill)

#Income Tax Calculator (basic)
income=float(input("Enter annual income: "))

if(income<=250000):
    tax=0
    dect_tax=income-tax
elif(income<=500000):
    tax=income*5/100 
    dect_tax=income-tax
else:
    tax=income*20/100
    dect_tax=income-tax
print("Income Tax = ₹", tax)
print("income after dectect tax:",dect_tax,)

#ATM Withdrawal Check (balance & amount)
balance=float(input("Enter balance: "))
amount=float(input("Enter wirhdrawal amount: "))

if amount<=balance:
    balance=balance-amount
    print("Withdrawal Successful")
    print("Remaining Balance:",balance)
else:
    print("Insufficient Balance")

#Login System (username and password)
user_name=input("Enter user name: ")
pass_word=(input("Enter password: "))

if(user_name=="Mario_prime" and pass_word=="Pankaj@9560"):
    print("Login Successful")
else:
    print("invalid user name and password!")
