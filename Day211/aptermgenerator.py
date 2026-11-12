def aptermgenerator():
    try:
        first_term = float(input("Enter first term: "))
        common_difference = float(input("Enter common difference: "))
        total_terms = int(input("Enter number of terms to generate: "))

        if total_terms <= 0:
            print("Number of terms must be greater than zero.")
            return

        print("\nGenerated Arithmetic Progression:")

        sequence = []

        for i in range(total_terms):
            term = first_term + i * common_difference
            sequence.append(term)

        print(", ".join(str(round(term, 4)) for term in sequence))

        print("\nTotal Terms:", total_terms)
        print("First Term:", first_term)
        print("Common Difference:", common_difference)
        print("Last Term:", round(sequence[-1], 4))

    except ValueError:
        print("Please enter valid numeric values.")

aptermgenerator()