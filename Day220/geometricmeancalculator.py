import math

def geometricmeancalculator():
    print("Geometric Mean Calculator")

    count = int(input("How many numbers do you want to enter? "))

    if count <= 0:
        print("Enter at least one number.")
        return

    product = 1

    for i in range(1, count + 1):
        number = float(input(f"Enter number {i}: "))

        if number < 0:
            print("Geometric mean is not defined for negative numbers in real numbers.")
            return

        product *= number

    geometric_mean = product ** (1 / count)

    print("\nProduct of Numbers =", product)
    print("Geometric Mean =", round(geometric_mean, 4))

geometricmeancalculator()