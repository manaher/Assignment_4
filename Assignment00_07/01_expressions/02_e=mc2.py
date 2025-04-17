C: int = 299792458 

def main():
    m = float(input("Enter the value of m in kg:"))

    e = m * C * C

    print("e = m * C**2")
    print(f"mass in kg = {m} kg")
    print(f"C = {C} m/s")
    print(f"e = {e} joules of energy")

if __name__ == '__main__':
    main()
