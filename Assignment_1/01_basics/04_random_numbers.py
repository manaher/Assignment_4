import random

def main():
    print("Printing 10 random numbers between 1-100:")
    for _ in range(10):
        print(random.randint(1, 100), end=', ')

if __name__ == '__main__':
    main()