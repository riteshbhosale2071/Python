def binomialexpansion():
    print("Binomial Expansion Generator :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    n = int(input("Enter the power n: "))

    if n < 0:
        print("Power must be a non-negative integer.")
        return

    coefficient = 1

    print("\nBinomial Expansion :")

    for r in range(n + 1):
        if r > 0:
            coefficient = coefficient * (n - r + 1) // r

        power_a = n - r
        power_b = r
        term = coefficient * (a ** power_a) * (b ** power_b)

        if r == 0:
            print(term, end="")
        elif term >= 0:
            print(" +", term, end="")
        else:
            print(" -", abs(term), end="")

    print()

binomialexpansion()