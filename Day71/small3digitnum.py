def small():
    digits = input("Enter three digits separated by space: ").split()

    digits.sort()

    smallest = "".join(digits)

    print("Smallest Number =", smallest)

small()