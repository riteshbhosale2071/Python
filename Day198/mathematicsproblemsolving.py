import math
from fractions import Fraction

def mathematicsproblemsolving():
    print("COMPLETE MATHEMATICS PROBLEM-SOLVING TOOLKIT :")

    def get_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Enter a numeric value.")
            return None

    def get_integer(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Enter an integer.")
            return None

    def read_list():
        try:
            values = input("Enter numbers separated by spaces: ").split()

            if not values:
                print("The list cannot be empty.")
                return None

            return [float(value) for value in values]
        except ValueError:
            print("Enter valid numeric values.")
            return None

    def statistics_tool():
        data = read_list()

        if data is None:
            return

        ordered = sorted(data)
        count = len(data)
        mean = sum(data) / count

        if count % 2 == 0:
            median = (ordered[count // 2 - 1] +
                      ordered[count // 2]) / 2
        else:
            median = ordered[count // 2]

        frequencies = {}
        for value in data:
            frequencies[value] = frequencies.get(value, 0) + 1

        highest_frequency = max(frequencies.values())
        modes = [
            value for value, frequency in frequencies.items()
            if frequency == highest_frequency
        ]

        variance = sum((value - mean) ** 2 for value in data) / count

        print("\nSorted Data:", ordered)
        print("Count:", count)
        print("Sum:", sum(data))
        print("Mean:", round(mean, 4))
        print("Median:", median)
        print("Mode:", modes if highest_frequency > 1 else "No repeated values")
        print("Minimum:", min(data))
        print("Maximum:", max(data))
        print("Range:", max(data) - min(data))
        print("Population Variance:", round(variance, 4))
        print("Population Standard Deviation:", round(math.sqrt(variance), 4))

    def linear_equation_tool():
        print("Solve an equation of the form ax + b = c")

        a = get_number("Enter a: ")
        if a is None:
            return

        b = get_number("Enter b: ")
        if b is None:
            return

        c = get_number("Enter c: ")
        if c is None:
            return

        if a == 0:
            if b == c:
                print("The equation has infinitely many solutions.")
            else:
                print("The equation has no solution.")
        else:
            x = (c - b) / a
            print("Equation:", a, "x +", b, "=", c)
            print("Solution: x =", x)
            print("Verification:", a * x + b, "=", c)

    def quadratic_equation_tool():
        print("Solve ax² + bx + c = 0")

        a = get_number("Enter coefficient a: ")
        if a is None:
            return

        b = get_number("Enter coefficient b: ")
        if b is None:
            return

        c = get_number("Enter coefficient c: ")
        if c is None:
            return

        if a == 0:
            print("This is not a quadratic equation.")
            if b != 0:
                print("Linear solution: x =", -c / b)
            elif c == 0:
                print("Infinitely many solutions.")
            else:
                print("No solution.")
            return

        discriminant = b * b - 4 * a * c
        print("Discriminant:", discriminant)

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print("Two distinct real roots:", x1, "and", x2)
        elif discriminant == 0:
            print("Repeated real root:", -b / (2 * a))
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / abs(2 * a)
            print("Complex roots:")
            print(real_part, "+", imaginary_part, "i")
            print(real_part, "-", imaginary_part, "i")

    def fraction_tool():
        print("Enter two rational numbers as integers or fractions.")
        try:
            first = Fraction(input("Enter first fraction: ").strip())
            second = Fraction(input("Enter second fraction: ").strip())
        except (ValueError, ZeroDivisionError):
            print("Invalid fraction.")
            return

        print("First simplified fraction:", first)
        print("Second simplified fraction:", second)
        print("Addition:", first + second)
        print("Subtraction:", first - second)
        print("Multiplication:", first * second)

        if second != 0:
            print("Division:", first / second)
        else:
            print("Division is undefined because the second fraction is zero.")

    def geometry_tool():
        print("\n1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Square")

        choice = input("Choose a shape: ").strip()

        if choice == "1":
            length = get_number("Enter length: ")
            if length is None:
                return

            width = get_number("Enter width: ")
            if width is None:
                return

            if length < 0 or width < 0:
                print("Dimensions cannot be negative.")
                return

            print("Area:", length * width)
            print("Perimeter:", 2 * (length + width))

        elif choice == "2":
            radius = get_number("Enter radius: ")
            if radius is None:
                return

            if radius < 0:
                print("Radius cannot be negative.")
                return

            print("Area:", round(math.pi * radius ** 2, 4))
            print("Circumference:", round(2 * math.pi * radius, 4))

        elif choice == "3":
            a = get_number("Enter first side: ")
            if a is None:
                return

            b = get_number("Enter second side: ")
            if b is None:
                return

            c = get_number("Enter third side: ")
            if c is None:
                return

            if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
                print("These sides do not form a valid triangle.")
                return

            perimeter = a + b + c
            semiperimeter = perimeter / 2
            area = math.sqrt(
                semiperimeter * (semiperimeter - a) *
                (semiperimeter - b) * (semiperimeter - c)
            )

            print("Perimeter:", perimeter)
            print("Area using Heron's formula:", round(area, 4))

        elif choice == "4":
            side = get_number("Enter side length: ")
            if side is None:
                return

            if side < 0:
                print("Side length cannot be negative.")
                return

            print("Area:", side ** 2)
            print("Perimeter:", 4 * side)

        else:
            print("Invalid shape selection.")

    def percentage_tool():
        value = get_number("Enter the number: ")
        if value is None:
            return

        percentage = get_number("Enter percentage: ")
        if percentage is None:
            return

        print(percentage, "% of", value, "=", value * percentage / 100)

    def probability_tool():
        favorable = get_integer("Enter favorable outcomes: ")
        if favorable is None:
            return

        total = get_integer("Enter total outcomes: ")
        if total is None:
            return

        if total <= 0 or favorable < 0 or favorable > total:
            print("Invalid outcome counts.")
            return

        probability = favorable / total
        print("Probability:", probability)
        print("Percentage:", round(probability * 100, 2), "%")

    def number_theory_tool():
        number = get_integer("Enter a positive integer: ")
        if number is None:
            return

        if number <= 0:
            print("Enter an integer greater than zero.")
            return

        divisors = [
            value for value in range(1, number + 1)
            if number % value == 0
        ]

        print("Divisors:", divisors)
        print("Number of Divisors:", len(divisors))

        if len(divisors) == 2:
            print("The number is prime.")
        else:
            print("The number is composite." if number > 1 else "Neither prime nor composite.")

        print("Square Root:", math.sqrt(number))
        print("Perfect Square:", math.isqrt(number) ** 2 == number)

    def ratio_tool():
        first = get_integer("Enter first ratio term: ")
        if first is None:
            return

        second = get_integer("Enter second ratio term: ")
        if second is None:
            return

        if first < 0 or second < 0 or (first == 0 and second == 0):
            print("Use non-negative terms, not both zero.")
            return

        common = math.gcd(first, second)

        print("Original Ratio:", str(first) + ":" + str(second))
        print("Simplified Ratio:",
              str(first // common) + ":" + str(second // common))

        total = first + second

        if total > 0:
            print("First Share Percentage:", round(first / total * 100, 2), "%")
            print("Second Share Percentage:", round(second / total * 100, 2), "%")

    def sequence_tool():
        first = get_number("Enter first term: ")
        if first is None:
            return

        difference = get_number("Enter common difference: ")
        if difference is None:
            return

        count = get_integer("Enter number of terms: ")
        if count is None:
            return

        if count <= 0:
            print("Number of terms must be positive.")
            return

        sequence = [
            first + i * difference for i in range(count)
        ]

        print("Arithmetic Sequence:", sequence)
        print("Nth Term:", sequence[-1])
        print("Sum of Terms:", sum(sequence))

    def simultaneous_equations_tool():
        print("Solve:")
        print("a1*x + b1*y = c1")
        print("a2*x + b2*y = c2")

        a1 = get_number("Enter a1: ")
        if a1 is None:
            return
        b1 = get_number("Enter b1: ")
        if b1 is None:
            return
        c1 = get_number("Enter c1: ")
        if c1 is None:
            return
        a2 = get_number("Enter a2: ")
        if a2 is None:
            return
        b2 = get_number("Enter b2: ")
        if b2 is None:
            return
        c2 = get_number("Enter c2: ")
        if c2 is None:
            return

        determinant = a1 * b2 - a2 * b1

        if determinant != 0:
            x = (c1 * b2 - c2 * b1) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            print("Unique solution:")
            print("x =", x)
            print("y =", y)
        elif a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("The equations have infinitely many solutions.")
        else:
            print("The equations have no solution.")

    while True:
        print("\n" + "=" * 55)
        print("MAIN MENU")
        print("1. Statistics Calculator")
        print("2. Linear Equation Solver")
        print("3. Quadratic Equation Solver")
        print("4. Fraction Calculator")
        print("5. Geometry Calculator")
        print("6. Percentage Calculator")
        print("7. Probability Calculator")
        print("8. Number Theory Analyzer")
        print("9. Ratio Simplifier")
        print("10. Arithmetic Sequence Calculator")
        print("11. Simultaneous Equation Solver")
        print("0. Exit")
        print("=" * 55)

        choice = input("Select a tool: ").strip()

        if choice == "1":
            statistics_tool()
        elif choice == "2":
            linear_equation_tool()
        elif choice == "3":
            quadratic_equation_tool()
        elif choice == "4":
            fraction_tool()
        elif choice == "5":
            geometry_tool()
        elif choice == "6":
            percentage_tool()
        elif choice == "7":
            probability_tool()
        elif choice == "8":
            number_theory_tool()
        elif choice == "9":
            ratio_tool()
        elif choice == "10":
            sequence_tool()
        elif choice == "11":
            simultaneous_equations_tool()
        elif choice == "0":
            print("Thank you for using the Mathematics Toolkit!")
            break
        else:
            print("Invalid selection. Choose an option from the menu.")

mathematicsproblemsolving()