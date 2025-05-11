def main():

    print("---PLANETARY WEIGHT CALCULATOR")
    print("MILESTONE#1- Mar's Weight")

    weight_on_earth= int(input("Enter your weight at earth: "))

    mars = 0.378

    weight_on_mars = weight_on_earth * mars
    rounded_weight= round(weight_on_mars, 2)

    print(f"Your weight on Planet Mars will be: {rounded_weight}")

if __name__ == '__main__':
    main()