#Number Guessing Game (Without Random)
secret=27
for attempt in range(5):
    guess=int(input("Enter the secret number: "))

    if(guess==secret):
     print("wow! this is correct")
     break 

    else:
     print("ohh! this is not")
     print("Try again")
print("Game Over")