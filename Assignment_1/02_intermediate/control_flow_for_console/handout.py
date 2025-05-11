import random

def main():
    print("*** WELCOME TO HIGH LOW GAME ***")

    score = 0

    for round_num in range(1, 6):
        print(f"\nRound: {round_num}")

        your_random_no = random.randint(1, 100)
        computer_random_no = random.randint(1, 100)

        print(f"Your number is {your_random_no}")

        guess = input("Do you think your number is higher or lower than the computer's? ").lower()

        while guess not in ["higher", "lower"]:
            guess = input("Please enter 'higher' or 'lower': ").lower()

        if guess == "lower" and your_random_no < computer_random_no:
            print(f"You were right! The computer's number was {computer_random_no}")
            score += 1

        elif guess == "higher" and your_random_no > computer_random_no:
            print(f"You were right! The computer's number was {computer_random_no}")
            score += 1

        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_random_no}")
            score -= 1

        print(f"Your score is now {score}")

    print(f"\n Your final score is: {score} out of 5")
    print("It was fun! Thanks for playing 😊")

if __name__ == '__main__':
    main()
