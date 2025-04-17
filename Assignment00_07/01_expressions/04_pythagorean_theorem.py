import math

def main():

    AB= float(input("Enter the length of AB: "))
    AC= float(input("Enter the length of AC: "))

    Length_of_BC = math.sqrt(AB ** 2 + AC ** 2)

    print(f"The length of BC is {Length_of_BC}")
    
if __name__ == '__main__':
    main()