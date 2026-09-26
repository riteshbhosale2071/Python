def equationtowordconverter():
    print("Equation-to-Word Converter :")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-hand side value: "))

        print("\nEquation:")
        print(a, "x +", b, "=", c)

        if a == 1:
            left_part = "x"
        elif a == -1:
            left_part = "negative x"
        else:
            left_part = str(a) + " times x"

        if b > 0:
            word_equation = left_part + " plus " + str(b) + " equals " + str(c)
        elif b < 0:
            word_equation = left_part + " minus " + str(abs(b)) + " equals " + str(c)
        else:
            word_equation = left_part + " equals " + str(c)

        print("\nWord Form:")
        print(word_equation)

    print("\nEquation-to-Word Conversion Completed.")

equationtowordconverter()