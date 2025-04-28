import random

def easy_mode():
    number = random.randint(1, 100)
    attempts = 10
    play(number, attempts)

def hard_mode():
    number = random.randint(1, 1000)
    attempts = 15
    play(number, attempts)

def play(number, attempt):
    print(f"Guess the number! You have {attempt} attempts.")
    while attempt > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == number:
                print(f"Congratulations! You guessed it right: {number}")
                return
            elif guess < number:
                print("Higher.")
            else:
                print("Lower.")
            attempt -= 1
            if attempt:
                print(f"Attempts left: {attempt}")
        except ValueError:
            print("Please enter a valid number.")
    print(f"Sorry, you lost. The number was {number}.")

 

while True:
    print("\n1. Easy Mode (1-100)")
    print("2. Hard Mode (1-1000)")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        easy_mode()
    elif choice == '2':
        hard_mode()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
