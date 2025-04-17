def average():
    
    first_number = int(input("Enter 1st number: "))
    second_number = int(input("Enter 2nd number: "))
    sum_of_numbers = first_number + second_number
    average = sum_of_numbers / 2

    print("The average of the two numbers is", average)
    
def main():

    average()
    
if __name__ == '__main__':
    main()