import random

while True:
    num=random.randint(1,10)
    guess=int(input("guess a number from 1 to 10:"))
    print(f"your guess={guess}")
    print(f"python={num}")

    if num==guess:
        print("your Guess is correct!")
    
    elif num!=guess:
        print("sorry,try again")    