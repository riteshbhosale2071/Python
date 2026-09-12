def polynomialdegreefinder():
    print("Polynomial Degree Finder :")

    polynomial = input("Enter a polynomial: ")

    degree = -1
    i = 0

    while i < len(polynomial):
        if polynomial[i] == "^":
            i = i + 1
            number = ""

            while i < len(polynomial) and polynomial[i].isdigit():
                number = number + polynomial[i]
                i = i + 1

            if number != "":
                power = int(number)

                if power > degree:
                    degree = power
        elif polynomial[i].lower() == "x":
            if degree < 1:
                degree = 1

        i = i + 1

    if degree == -1:
        degree = 0

    print("Degree of polynomial:", degree)

polynomialdegreefinder()