import math

def irrationalnumber():
    number = float(input("Enter a number: "))

    if math.isclose(number, round(number), rel_tol=1e-12, abs_tol=1e-12):
        print("The number is Rational.")
        return

    if number >= 0:
        root = math.sqrt(number)

        if math.isclose(root, round(root), rel_tol=1e-12, abs_tol=1e-12):
            print("The number is Rational.")
            return

    print("The number is Irrational.")

irrationalnumber()