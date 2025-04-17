def add_numbers(numbers)-> int:

    total: int = 0
    for i in numbers:
        total += i

    return total
    
def main():
    numbers: list[int] = [1,2,3,4,5]
    sum : int = add_numbers(numbers)
    print(sum)

if __name__ == '__main__':
    main()