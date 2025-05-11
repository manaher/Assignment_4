import random

def main():
    
    random_number = random.randint(1, 3)  # 1 dafa hi generate hoga
    user_input = int(input("Guess the number: "))  # Step 1

    while user_input != random_number:             # Jab tak galat hai
        if user_input < random_number:
            print("Your guess is too low!")
        elif user_input > random_number:
            print("Your guess is too high!")

        user_input = int(input("Enter a new number: "))  # Step 2 — guess dobara lo

    print("Congrats! Your guess is right")  # Jab match ho gaya

if __name__ == '__main__':
    main()