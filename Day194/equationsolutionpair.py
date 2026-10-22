def equationsolutionpair():
    print("Equation Solution Pair Generator :")
    print("Equation format: ax + by = c")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter constant c: "))
        limit = int(input("Enter the range limit for x and y: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if limit < 0:
        print("Range limit cannot be negative.")
        return

    if a == 0 and b == 0:
        if c == 0:
            print("Every integer pair is a solution within the given range.")
        else:
            print("No solution exists for this equation.")
        return

    solutions = []

    for x in range(-limit, limit + 1):
        for y in range(-limit, limit + 1):
            if abs(a * x + b * y - c) < 0.000001:
                solutions.append((x, y))

    print("\nSolution Pairs :")

    if solutions:
        for index, pair in enumerate(solutions, start=1):
            print("Pair", index, ": x =", pair[0], ", y =", pair[1])

        print("\nTotal Solution Pairs:", len(solutions))
    else:
        print("No integer solution pairs found in the given range.")

    print("\nVerification :")

    for x, y in solutions:
        result = a * x + b * y
        print(
            "x =", x,
            ", y =", y,
            "=>",
            a, "*", x, "+", b, "*", y, "=",
            round(result, 4),
            "| Expected:", c
        )

    print("\nSearch Range:")
    print("x:", -limit, "to", limit)
    print("y:", -limit, "to", limit)

equationsolutionpair()