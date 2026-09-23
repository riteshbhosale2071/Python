def missingpolynomialterm():
    print("Missing Polynomial Term Finder :")

    degree = int(input("Enter the degree of the polynomial: "))
    missing_power = int(input("Enter the power of the missing term: "))
    x = float(input("Enter the value of x: "))
    expected_value = float(input("Enter the expected polynomial value: "))

    if degree >= 0 and 0 <= missing_power <= degree:
        known_value = 0

        for power in range(degree, -1, -1):
            if power == missing_power:
                continue

            coefficient = float(input("Enter coefficient of x^" + str(power) + ": "))
            known_value += coefficient * (x ** power)

        missing_power_value = x ** missing_power

        if missing_power_value != 0:
            missing_coefficient = (expected_value - known_value) / missing_power_value

            print("Missing Term Coefficient:", round(missing_coefficient, 2))
            print("Missing Term:", round(missing_coefficient, 2), "x^" + str(missing_power))
        else:
            if expected_value == known_value:
                print("The missing coefficient cannot be uniquely determined.")
            else:
                print("No valid missing coefficient exists for the given values.")
    else:
        print("Enter a valid polynomial degree and missing power.")

missingpolynomialterm()