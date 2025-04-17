import random

def main():

    NUM_SIDES = 6

    die1 = random.randint(1,NUM_SIDES)
    die2 = random.randint(2,NUM_SIDES)
    total = die1 + die2

    print(f"Each dice has {NUM_SIDES} sides")
    print(f"The result of rolling first dice is: {die1}")
    print(f"The result of rolling second dice is: {die2}")
    print(f"The sum of the results of the two dice is: {total}")

if __name__ == '__main__':
    main()