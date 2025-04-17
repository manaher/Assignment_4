def double(num):
    number= num * 2
    print(f"The double of {num} is {number} ")
    

def main():
    num = int(input("Enter a number to double it: "))
    double(num)

if __name__ == '__main__':
    main()