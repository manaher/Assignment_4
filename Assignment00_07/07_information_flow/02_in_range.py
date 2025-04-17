def main():
    
    number = 5
    if in_range(number, 1, 10):
        print(f"{number} is in range.")
    else:
        print(f"{number} is not in range.")

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

if __name__ == '__main__':
    main()
