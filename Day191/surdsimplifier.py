def surdsimplifier():
    print("Surd Simplifier :")

    try:
        coefficient = int(input("Enter the coefficient of the surd: "))
        number = int(input("Enter the number inside the square root: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if number < 0:
        print("This program simplifies real square-root surds only.")
        return

    if coefficient == 0 or number == 0:
        print("Simplified Result: 0")
        return

    outside = 1
    inside = number
    factor = 2

    while factor * factor <= inside:
        while inside % (factor * factor) == 0:
            inside //= factor * factor
            outside *= factor
        factor += 1

    simplified_coefficient = coefficient * outside

    print("\nSimplification Results :")
    print("Original Expression:", coefficient, "√", number)

    if inside == 1:
        print("Simplified Result:", simplified_coefficient)
    elif simplified_coefficient == 1:
        print("Simplified Result: √", inside)
    elif simplified_coefficient == -1:
        print("Simplified Result: -√", inside)
    else:
        print("Simplified Result:", simplified_coefficient, "√", inside)

    print("\nVerification :")
    print("Original Value:", round(coefficient * (number ** 0.5), 6))
    print("Simplified Value:", round(simplified_coefficient * (inside ** 0.5), 6))

    if inside == 1:
        print("Classification: The result is an integer.")
    else:
        print("Classification: The result contains a simplified surd.")

surdsimplifier()