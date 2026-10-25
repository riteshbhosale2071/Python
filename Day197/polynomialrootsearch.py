def polynomialrootsearch():
    print("Polynomial Root Search :")
    print("Enter polynomial coefficients in descending powers.")
    print("Example: 1, -5, 6 represents x² - 5x + 6")

    def evaluate_polynomial(coefficients, x):
        result = 0

        for coefficient in coefficients:
            result = result * x + coefficient

        return result

    def read_coefficients():
        try:
            values = input("Enter coefficients separated by commas: ")
            coefficients = [float(value.strip()) for value in values.split(",")]

            if not coefficients:
                return None

            while len(coefficients) > 1 and coefficients[0] == 0:
                coefficients.pop(0)

            if any(not value.is_integer() for value in coefficients):
                print("Note: Rational-root testing is designed for integer coefficients.")

            return coefficients
        except ValueError:
            print("Invalid coefficients. Enter numeric values.")
            return None

    coefficients = read_coefficients()

    if coefficients is None:
        return

    if all(value == 0 for value in coefficients):
        print("The zero polynomial has every number as a root.")
        return

    degree = len(coefficients) - 1

    print("\nPolynomial degree:", degree)

    if degree == 0:
        print("A non-zero constant polynomial has no roots.")
        return

    print("\nChoose root search method:")
    print("1. Search integer roots within a range")
    print("2. Search approximate real roots within a range")
    print("3. Test rational root candidates")

    choice = input("Enter your choice (1-3): ").strip()

    roots = []

    if choice == "1":
        try:
            start = int(input("Enter starting integer: "))
            end = int(input("Enter ending integer: "))
        except ValueError:
            print("Enter valid integers.")
            return

        if start > end:
            print("Starting value must not exceed ending value.")
            return

        for x in range(start, end + 1):
            if abs(evaluate_polynomial(coefficients, x)) < 1e-9:
                roots.append(x)

    elif choice == "2":
        try:
            start = float(input("Enter starting value: "))
            end = float(input("Enter ending value: "))
            step = float(input("Enter search step, e.g. 0.1: "))
        except ValueError:
            print("Enter valid numeric values.")
            return

        if start >= end or step <= 0:
            print("End must exceed start and step must be positive.")
            return

        if (end - start) / step > 1000000:
            print("Search range is too large. Use a larger step.")
            return

        x = start
        previous_x = x
        previous_y = evaluate_polynomial(coefficients, x)

        if abs(previous_y) < 1e-9:
            roots.append(round(x, 8))

        while x < end:
            x = min(x + step, end)
            current_y = evaluate_polynomial(coefficients, x)

            if abs(current_y) < 1e-9:
                root = round(x, 8)

                if not any(abs(root - r) < step / 2 for r in roots):
                    roots.append(root)

            elif previous_y * current_y < 0:
                left = previous_x
                right = x
                left_y = previous_y

                for _ in range(100):
                    middle = (left + right) / 2
                    middle_y = evaluate_polynomial(coefficients, middle)

                    if abs(middle_y) < 1e-12:
                        left = middle
                        right = middle
                        break

                    if left_y * middle_y < 0:
                        right = middle
                    else:
                        left = middle
                        left_y = middle_y

                root = round((left + right) / 2, 8)

                if not any(abs(root - r) < step / 2 for r in roots):
                    roots.append(root)

            previous_x = x
            previous_y = current_y

    elif choice == "3":
        if not all(value.is_integer() for value in coefficients):
            print("Rational-root testing requires integer coefficients.")
            return

        integer_coefficients = [int(value) for value in coefficients]

        def divisors(number):
            number = abs(number)

            if number == 0:
                return [0]

            result = []

            for value in range(1, number + 1):
                if number % value == 0:
                    result.append(value)

            return result

        constant = integer_coefficients[-1]
        leading = integer_coefficients[0]

        if constant == 0:
            print("0 is a root because the constant term is zero.")

        if constant != 0:
            numerator_values = divisors(constant)
            denominator_values = divisors(leading)
            candidates = set()

            for numerator in numerator_values:
                for denominator in denominator_values:
                    from fractions import Fraction

                    candidate = Fraction(numerator, denominator)
                    candidates.add(candidate)
                    candidates.add(-candidate)

            for candidate in sorted(candidates):
                if evaluate_polynomial(coefficients, float(candidate)) == 0:
                    roots.append(candidate)

        elif degree > 1:
            reduced = integer_coefficients[:-1]

            print("After factoring out x, test the reduced polynomial:")
            print("Reduced coefficients:", reduced)

        if 0 in roots:
            roots.remove(0)

        if constant == 0:
            roots.insert(0, 0)

    else:
        print("Invalid choice.")
        return

    print("\nRoot Search Results :")

    if roots:
        for root in sorted(set(roots), key=float):
            print("Root:", root)
            print("Polynomial value:", evaluate_polynomial(coefficients, float(root)))
    else:
        print("No roots found using the selected search method.")

    print("\nNote: Numerical searches may miss repeated roots or roots")
    print("outside the selected range. Rational-root testing checks")
    print("candidates for polynomials with integer coefficients.")

    print("\nPolynomial root search completed.")

polynomialrootsearch()