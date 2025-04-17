SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():

    adjective = str(input("Please enter an adjective: "))
    noun = str(input("Please enter a noun: "))
    verb = str(input("Please enter a verb:"))

    print(f"{SENTENCE_START} {adjective} {noun} {verb}")
    # print(SENTENCE_START + adjective + " " + noun + " " + verb + "!") also can be done in this way

if __name__ == '__main__':
    main()

