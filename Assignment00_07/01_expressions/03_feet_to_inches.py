def main():

    Feet = float(input("Enter the value in foot(or feet) to get measuremnt in inches:"))

    Measurement_in_inches = Feet * 12

    print(f"{Feet} = {Measurement_in_inches} inches")

if __name__ == '__main__':
    main()