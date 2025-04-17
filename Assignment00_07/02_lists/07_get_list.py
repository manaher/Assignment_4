def main():
    lst = []

    val = input("Enter a value: ")  # Initial value
    while val:  # tab chalega jab user ny empty value na di ho
        lst.append(val)
        val = input("Enter a value: ")  # next value

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()