def expansionverification():
    print("Expansion Verification Program :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    n = int(input("Enter power n: "))

    if n < 0:
        print("Power must be a non-negative integer.")
        return

    original = (a + b) ** n
    expanded = 0
    coefficient = 1

    for r in range(n + 1):
        if r > 0:
            coefficient = coefficient * (n - r + 1) // r

        term = coefficient * (a ** (n - r)) * (b ** r)
        expanded = expanded + term

    print("\nVerification :")
    print("Original expression value:", original)
    print("Expanded expression value:", expanded)

    if original == expanded:
        print("Expansion verified successfully.")
    else:
        print("Expansion is incorrect.")

expansionverification()