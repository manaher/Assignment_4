Max_length : int = 3

def shorten(lst):
    while len(lst) > Max_length:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()