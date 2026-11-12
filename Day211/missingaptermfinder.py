def missingaptermfinder():
    try:
        first_term = float(input("Enter first term: "))
        common_difference = float(input("Enter common difference: "))
        total_terms = int(input("Enter total number of terms: "))
        missing_position = int(input("Enter position of missing term: "))

        if total_terms < 1 or missing_position < 1 or missing_position > total_terms:
            print("Invalid term count or missing position.")
            return

        missing_term = first_term + (missing_position - 1) * common_difference

        print("\nMissing AP Term:", round(missing_term, 4))

        print("\nComplete Arithmetic Progression:")
        sequence = [
            first_term + i * common_difference
            for i in range(total_terms)
        ]

        sequence[missing_position - 1] = missing_term

        print(", ".join(str(round(term, 4)) for term in sequence))

    except ValueError:
        print("Please enter valid numeric values.")

missingaptermfinder()