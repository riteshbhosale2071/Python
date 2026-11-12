def nthtermcalculator():
    try:
        first_term = float(input("Enter first term (a): "))
        common_difference = float(input("Enter common difference (d): "))
        n = int(input("Enter term number (n): "))

        if n <= 0:
            print("Term number must be greater than zero.")
            return

        nth_term = first_term + (n - 1) * common_difference

        print("\nNth Term of Arithmetic Progression:")
        print("First Term:", first_term)
        print("Common Difference:", common_difference)
        print("Term Number:", n)
        print("Nth Term:", round(nth_term, 4))

    except ValueError:
        print("Please enter valid numeric values.")

nthtermcalculator()