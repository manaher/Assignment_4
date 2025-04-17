def print_ones_digit(num):
    value = num % 10
    print(f"The one digit is: {value}" )

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()