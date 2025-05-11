def mad_libs():
    print("Let\'s play MAdlibs! fill in the blanks with your own words.")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me a funny adjective: ")
    random_obj= input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f'''
    Once upon a time, there was a person named {name} who lived in {place}.
    One day they found a {funny_adj} {random_obj}that belonged to an {animal}.
    The {animal} was very upset and started to {action_verb} around.
    {name} couldn't help but laugh and shouted "{funny_exclamation}!".'''
    
    print(f"\n Here is your Madlib story: {story}")

if __name__ == '__main__':
    mad_libs()
