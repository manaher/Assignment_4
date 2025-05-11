def main():

    current_number = int(input("Enter a number to double it: "))
    curr_value = current_number * 2 #ye line aik bar double karegi

    while curr_value < 100:
        print(curr_value)
        curr_value *= 2 #isline se jo bhi number aayega wo bar bar double hoga


if __name__ == '__main__':
    main()