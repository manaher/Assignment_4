# Mercury = 0.376
# Venus = 0.889
# Mars = 0.378
# Jupiter = 2.360
# Saturn = 1.081
# Uranus = 0.815
# Neptune = 1.140

# def main():

#     print("MILETSONE#2- Adding in all Planets")

#     weight_on_earth= int(input("Please enter your weight on Earth: "))

#     choose = input("Please enter the planet name: ").capitalize()

#     if choose == "Mercury":
#         wt_on_mercury = weight_on_earth * Mercury
#         rounded_weight1 = round(wt_on_mercury, 2)
#         print(rounded_weight1)

#     elif choose == "Venus":
#         wt_on_venus = weight_on_earth * Venus
#         rounded_weight2 = round(wt_on_venus, 2)
#         print(rounded_weight2)

#     elif choose == "Mars":
#         wt_on_mars = weight_on_earth * Mars
#         rounded_weight3 = round(wt_on_mars, 2)
#         print(rounded_weight3)

#     elif choose == "Jupiter":
#         wt_on_jupiter = weight_on_earth * Jupiter
#         rounded_weight4 = round(wt_on_jupiter, 2)
#         print(rounded_weight4)

#     elif choose == "Saturn":
#         wt_on_saturn = weight_on_earth * Saturn
#         rounded_weight5 = round(wt_on_saturn, 2)
#         print(rounded_weight5)

#     elif choose == "Uranus":
#         wt_on_uranus = weight_on_earth * Uranus
#         rounded_weight6 = round(wt_on_uranus, 2)
#         print(rounded_weight6)

#     elif choose == "Neptune":
#         wt_on_neptune = weight_on_earth * Neptune
#         rounded_weight7 = round(wt_on_neptune, 2)
#         print(rounded_weight7)
        
#     else:
#         print("The conversion is not possible")

# if __name__ == '__main__':
#     main()

# planet_gravity = {
#     "Mercury": 0.376,
#     "Venus": 0.889,
#     "Mars": 0.378,
#     "Jupiter": 2.360,
#     "Saturn": 1.081,
#     "Uranus": 0.815,
#     "Neptune": 1.140
# }
# weight_on_earth = int(input("Please input your weight on earth: "))
# choose = input(f"Choose a planet from: {', '.join(planet_gravity.keys())}\n")

# if choose in planet_gravity:
#     weight_on_planet = round(weight_on_earth * planet_gravity[choose], 2)
#     print(f"Your weight on {choose} would be: {weight_on_planet}")
# else:
#     print("Invalid planet name.")

Mercury = 0.376
Venus = 0.889
Mars = 0.378
Jupiter = 2.360
Saturn = 1.081
Uranus = 0.815
Neptune = 1.140

def main():

    print("MILETSONE#2- Adding in all Planets")

    weight_on_earth= int(input("Please enter your weight on Earth: "))

    choose = input("Please enter the planet name: ").capitalize()

    if choose == "Mercury":
        gravity_const = Mercury

    elif choose == "Venus":
        gravity_const = Venus

    elif choose == "Mars":
        gravity_const = Mars

    elif choose == "Jupiter":
        gravity_const = Jupiter

    elif choose == "Saturn":
        gravity_const = Saturn

    elif choose == "Uranus":
        gravity_const = Uranus

    elif choose == "Neptune":
        gravity_const = Neptune
        
    else:
        print("The conversion not possible")

        return

    # Calculating result
    weight_on_planet = weight_on_earth * gravity_const
    rounded_weight = round(weight_on_planet, 2)

    # Display result
    print(f"The weight at {choose} planet would be: {rounded_weight}")

if __name__ == '__main__':
    main()


