def mathematicalpatternmining():
    print("Mathematical Pattern Mining :")

    number_of_terms = int(input("Enter number of terms: "))

    if number_of_terms < 3:
        print("Enter at least 3 terms.")
        return

    terms = []

    for i in range(number_of_terms):
        value = float(input("Enter term " + str(i + 1) + ": "))
        terms.append(value)

    print("\nPattern Analysis :")

    differences = []

    for i in range(number_of_terms - 1):
        differences.append(terms[i + 1] - terms[i])

    same_difference = True

    for i in range(1, len(differences)):
        if differences[i] != differences[0]:
            same_difference = False
            break

    if same_difference:
        print("Pattern Type: Arithmetic Sequence")
        print("Common Difference:", round(differences[0], 2))
        print("Next Term:", round(terms[-1] + differences[0], 2))
        return

    ratios = []

    valid_ratio = True

    for i in range(number_of_terms - 1):
        if terms[i] == 0:
            valid_ratio = False
            break
        ratios.append(terms[i + 1] / terms[i])

    if valid_ratio:
        same_ratio = True

        for i in range(1, len(ratios)):
            if ratios[i] != ratios[0]:
                same_ratio = False
                break

        if same_ratio:
            print("Pattern Type: Geometric Sequence")
            print("Common Ratio:", round(ratios[0], 2))
            print("Next Term:", round(terms[-1] * ratios[0], 2))
            return

    second_differences = []

    for i in range(len(differences) - 1):
        second_differences.append(differences[i + 1] - differences[i])

    same_second_difference = True

    for i in range(1, len(second_differences)):
        if second_differences[i] != second_differences[0]:
            same_second_difference = False
            break

    if same_second_difference:
        print("Pattern Type: Quadratic Pattern")
        print("Second Difference:", round(second_differences[0], 2))
        next_difference = differences[-1] + second_differences[0]
        next_term = terms[-1] + next_difference
        print("Next Term:", round(next_term, 2))
    else:
        print("Pattern Type: Irregular or Complex Pattern")
        print("No simple arithmetic, geometric, or quadratic pattern detected.")

mathematicalpatternmining()