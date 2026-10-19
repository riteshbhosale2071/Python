def surdgrouping():
    print("Surd Grouping Program :")

    n = int(input("Enter the number of surds: "))

    if n <= 0:
        print("Number of surds must be greater than zero.")
        return

    surds = []

    for i in range(n):
        print("\nSurd", i + 1)

        coefficient = int(input("Enter the coefficient: "))
        number = int(input("Enter the number inside the square root: "))

        if number < 0:
            print("Negative values inside square roots are not supported.")
            return

        if number == 0 or coefficient == 0:
            surds.append((0, 1))
            continue

        outside = 1
        inside = number
        factor = 2

        while factor * factor <= inside:
            while inside % (factor * factor) == 0:
                inside //= factor * factor
                outside *= factor
            factor += 1

        simplified_coefficient = coefficient * outside
        surds.append((simplified_coefficient, inside))

    groups = {}

    for coefficient, radicand in surds:
        if radicand in groups:
            groups[radicand] += coefficient
        else:
            groups[radicand] = coefficient

    print("\nSimplified Surds :")

    for coefficient, radicand in surds:
        if coefficient == 0:
            print("0")
        elif radicand == 1:
            print(coefficient)
        elif coefficient == 1:
            print("√" + str(radicand))
        elif coefficient == -1:
            print("-√" + str(radicand))
        else:
            print(str(coefficient) + "√" + str(radicand))

    print("\nSurd Groups :")

    for radicand, coefficient in groups.items():
        if coefficient == 0:
            print("√" + str(radicand) + " group: Sum = 0")
        elif radicand == 1:
            print("Integer group: Sum =", coefficient)
        elif coefficient == 1:
            print("√" + str(radicand) + " group: Sum = √" + str(radicand))
        elif coefficient == -1:
            print("√" + str(radicand) + " group: Sum = -√" + str(radicand))
        else:
            print("√" + str(radicand) + " group: Sum =",
                  str(coefficient) + "√" + str(radicand))

    print("\nFinal Combined Expression :")

    terms = []

    for radicand, coefficient in groups.items():
        if coefficient == 0:
            continue
        elif radicand == 1:
            terms.append(str(coefficient))
        elif coefficient == 1:
            terms.append("√" + str(radicand))
        elif coefficient == -1:
            terms.append("-√" + str(radicand))
        else:
            terms.append(str(coefficient) + "√" + str(radicand))

    if len(terms) == 0:
        print("0")
    else:
        expression = terms[0]

        for term in terms[1:]:
            if term.startswith("-"):
                expression += " - " + term[1:]
            else:
                expression += " + " + term

        print(expression)

surdgrouping()