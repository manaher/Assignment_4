def main():

    day_in_year = 365
    hours_per_day = 24
    min_per_hour= 60
    seconds_per_min = 60

    num_of_seconds_per_year = day_in_year * hours_per_day * min_per_hour * seconds_per_min

    print(f"There are {num_of_seconds_per_year} seconds in a year!")

if __name__ == '__main__':
    main()