import random
print("Welcome to the NUmber Guessing Game!")

secret_number = random.randint(1, 10)
print("I have secret number between 1 and 10. Can u guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high try again.")
        elif guess < secret_number:
            print("Too low try again.")
        else:
            print("Congratulations u have guesses the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")