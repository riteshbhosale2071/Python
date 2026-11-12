def sumofnaptermscalculator():
    try:
        first_term = float(input("Enter first term (a): "))
        common_difference = float(input("Enter common difference (d): "))
        n = int(input("Enter number of terms (n): "))

        if n <= 0:
            print("Number of terms must be greater than zero.")
            return

        last_term = first_term + (n - 1) * common_difference
        total_sum = (n / 2) * (first_term + last_term)

        print("\nArithmetic Progression Details:")
        print("First Term:", first_term)
        print("Common Difference:", common_difference)
        print("Number of Terms:", n)
        print("Last Term:", round(last_term, 4))
        print("Sum of AP Terms:", round(total_sum, 4))

    except ValueError:
        print("Please enter valid numeric values.")

sumofnaptermscalculator()