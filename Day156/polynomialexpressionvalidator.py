def polynomialexpressionvalidator():
    print("Polynomial Expression Validator :")

    polynomial = input("Enter polynomial: ")
    polynomial = polynomial.replace(" ", "")

    if polynomial == "":
        print("Invalid polynomial.")
        return

    i = 0
    valid = True
    term_count = 0

    while i < len(polynomial):
        if polynomial[i] == "+" or polynomial[i] == "-":
            i = i + 1

            if i >= len(polynomial):
                valid = False
                break

        coefficient_found = False

        while i < len(polynomial) and polynomial[i].isdigit():
            coefficient_found = True
            i = i + 1

        if i < len(polynomial) and polynomial[i] == "x":
            i = i + 1

            if i < len(polynomial) and polynomial[i] == "^":
                i = i + 1

                if i >= len(polynomial) or not polynomial[i].isdigit():
                    valid = False
                    break

                while i < len(polynomial) and polynomial[i].isdigit():
                    i = i + 1

            term_count = term_count + 1
            continue

        if coefficient_found:
            term_count = term_count + 1
            continue

        valid = False
        break

    if valid and term_count > 0:
        print("Valid polynomial expression.")
        print("Number of terms:", term_count)
    else:
        print("Invalid polynomial expression.")

polynomialexpressionvalidator()