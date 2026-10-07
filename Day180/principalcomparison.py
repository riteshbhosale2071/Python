def principalcomparison():
    print("Principal Comparison :")

    principal1 = float(input("Enter first principal amount: "))
    principal2 = float(input("Enter second principal amount: "))

    if principal1 < 0 or principal2 < 0:
        print("Principal amounts cannot be negative.")
        return

    difference = abs(principal1 - principal2)

    if principal1 > principal2:
        larger = principal1
        smaller = principal2
        print("\nFirst principal is larger.")
    elif principal2 > principal1:
        larger = principal2
        smaller = principal1
        print("\nSecond principal is larger.")
    else:
        larger = principal1
        smaller = principal2
        print("\nBoth principal amounts are equal.")

    print("First Principal:", round(principal1, 2))
    print("Second Principal:", round(principal2, 2))
    print("Difference:", round(difference, 2))

    if smaller > 0:
        percentage_difference = (difference / smaller) * 100
        print("Percentage Difference:", round(percentage_difference, 2), "%")
    else:
        print("Percentage Difference: Cannot be calculated.")

principalcomparison()