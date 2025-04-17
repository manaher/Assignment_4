def main():

    dividend= int(input("Enter a number to be divided: "))
    divisor= int(input("Enter a number to be divided by: "))

    result_of_division= dividend / divisor
    remainder= dividend % divisor

    print(f"The result of the division is {result_of_division} and the remainder is {remainder}")

if __name__ == '__main__':
    main()