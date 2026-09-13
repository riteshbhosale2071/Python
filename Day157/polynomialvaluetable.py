def polynomialvaluetable():
    print("Polynomial Value Table Generator :")

    polynomial = input("Enter polynomial: ")
    start = float(input("Enter starting value of x: "))
    end = float(input("Enter ending value of x: "))
    step = float(input("Enter step value: "))

    if step <= 0 or start > end:
        print("Invalid range or step value.")
        return

    polynomial = polynomial.replace(" ", "")

    def evaluate(x):
        terms = polynomial.replace("-", "+-").split("+")
        result = 0

        for term in terms:
            if term == "":
                continue

            if "x^" in term:
                parts = term.split("x^")
                coefficient = parts[0]
                power = int(parts[1])

                if coefficient == "":
                    coefficient = 1
                elif coefficient == "-":
                    coefficient = -1
                else:
                    coefficient = int(coefficient)

                result = result + coefficient * (x ** power)

            elif "x" in term:
                parts = term.split("x")

                if parts[0] == "":
                    coefficient = 1
                elif parts[0] == "-":
                    coefficient = -1
                else:
                    coefficient = int(parts[0])

                result = result + coefficient * x

            else:
                result = result + int(term)

        return result

    print("\nPolynomial Value Table :")
    print("x\t\tP(x)")

    x = start

    while x <= end + step / 1000:
        value = evaluate(x)
        print("{:.2f}\t\t{:.2f}".format(x, value))
        x = x + step

polynomialvaluetable()