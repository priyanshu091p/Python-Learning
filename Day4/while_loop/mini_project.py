#ATM System

'''Features:
Check Balance
Deposit Money
Withdraw Money
Exit

Use:
while
if-elif
break'''

balance=23000
pin=1234

user_pin=int(input("Enter your pin: "))

if(pin==user_pin):
    while True:
        print("\n-----Menu-----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice=int(input("Entere your choice: "))

        if(choice==1):
            print(f"Balance : {balance}")

        elif(choice==2):
            amount=int(input("Enter Deposit Amount: "))
            balance=balance+amount
            print(f"New Balance : {balance}")

        elif(choice==3):
            amount=int(input("Enter Withdraw Amount: "))

            if(amount<=balance):
                balance=balance-amount
                print(f"Remaining Balance : {balance}")
            else:
                print("Insufficient Balance.")

        elif(choice==4):
            print("Thanks for using ATM")
            break
        
        else:
             print("Invalid choice. Try again.")

else:
    print("Incorrect Pin.")
        
