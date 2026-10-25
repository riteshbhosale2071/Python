import math
from fractions import Fraction

def rationalandsurdexpression():
    print("Rational and Surd Expression Evaluator :")

    def read_fraction(prompt):
        try:
            value = input(prompt).strip()
            number = Fraction(value)

            return number
        except (ValueError, ZeroDivisionError):
            print("Invalid rational number.")
            return None

    def simplify_surd(number):
        if number < 0:
            return "Invalid: negative square root is not real"

        if number == 0:
            return "0"

        outside = 1
        inside = number
        factor = 2

        while factor * factor <= inside:
            while inside % (factor * factor) == 0:
                inside //= factor * factor
                outside *= factor
            factor += 1

        if inside == 1:
            return str(outside)

        if outside == 1:
            return "√" + str(inside)

        return str(outside) + "√" + str(inside)

    print("\nChoose an operation:")
    print("1. Add rational numbers")
    print("2. Subtract rational numbers")
    print("3. Multiply rational numbers")
    print("4. Divide rational numbers")
    print("5. Evaluate a square root")
    print("6. Add square roots with integer radicands")
    print("7. Multiply square roots with integer radicands")
    print("8. Add a rational number and a surd")
    print("9. Evaluate a rational number plus a square root")

    choice = input("\nEnter your choice (1-9): ").strip()

    if choice in ["1", "2", "3", "4"]:
        a = read_fraction("Enter the first rational number (e.g. 3/4): ")

        if a is None:
            return

        b = read_fraction("Enter the second rational number: ")

        if b is None:
            return

        if choice == "1":
            result = a + b
            operation = "Addition"
        elif choice == "2":
            result = a - b
            operation = "Subtraction"
        elif choice == "3":
            result = a * b
            operation = "Multiplication"
        else:
            if b == 0:
                print("Division by zero is not allowed.")
                return

            result = a / b
            operation = "Division"

        print("\nOperation:", operation)
        print("Exact Result:", result)
        print("Decimal Result:", float(result))

    elif choice == "5":
        try:
            number = int(input("Enter a non-negative integer: "))
        except ValueError:
            print("Please enter an integer.")
            return

        if number < 0:
            print("Negative numbers do not have real square roots.")
            return

        print("Simplified Surd:", simplify_surd(number))
        print("Decimal Value:", math.sqrt(number))

    elif choice in ["6", "7"]:
        try:
            a = int(input("Enter the first non-negative radicand: "))
            b = int(input("Enter the second non-negative radicand: "))
        except ValueError:
            print("Please enter integers.")
            return

        if a < 0 or b < 0:
            print("Radicands must be non-negative.")
            return

        if choice == "6":
            print("\nFirst Surd:", simplify_surd(a))
            print("Second Surd:", simplify_surd(b))
            print("Decimal Sum:", math.sqrt(a) + math.sqrt(b))

            if a == b:
                print("Exact Sum:", simplify_surd(4 * a))
            else:
                print("Exact Sum: √" + str(a) + " + √" + str(b))
        else:
            product = a * b
            print("\nProduct Under Square Root:", product)
            print("Simplified Product:", simplify_surd(product))
            print("Decimal Product:", math.sqrt(a) * math.sqrt(b))

    elif choice == "8":
        rational = read_fraction("Enter a rational number (e.g. 3/2): ")

        if rational is None:
            return

        try:
            radicand = int(input("Enter a non-negative integer radicand: "))
        except ValueError:
            print("Please enter an integer.")
            return

        if radicand < 0:
            print("Radicand must be non-negative.")
            return

        print("\nRational Part:", rational)
        print("Surd Part:", simplify_surd(radicand))
        print("Decimal Result:", float(rational) + math.sqrt(radicand))

        if math.isqrt(radicand) ** 2 == radicand:
            exact = rational + math.isqrt(radicand)
            print("Exact Result:", exact)
        else:
            print("Exact Result:", str(rational) + " + √" + str(radicand))

    elif choice == "9":
        rational = read_fraction("Enter a rational number (e.g. 2/3): ")

        if rational is None:
            return

        try:
            radicand = int(input("Enter a non-negative integer radicand: "))
        except ValueError:
            print("Please enter an integer.")
            return

        if radicand < 0:
            print("Radicand must be non-negative.")
            return

        print("\nExpression:", str(rational) + " + √" + str(radicand))
        print("Decimal Result:", float(rational) + math.sqrt(radicand))

        root = math.isqrt(radicand)

        if root * root == radicand:
            print("Exact Result:", rational + root)
        else:
            print("Exact Result:", str(rational) + " + √" + str(radicand))

    else:
        print("Invalid choice. Please select a number from 1 to 9.")

    print("\nEvaluation completed.")

rationalandsurdexpression()