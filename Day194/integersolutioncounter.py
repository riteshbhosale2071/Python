def integersolutioncounter():
    print("Integer Solution Counter :")
    print("Equation format: ax + by = c")

    try:
        a = int(input("Enter coefficient a: "))
        b = int(input("Enter coefficient b: "))
        c = int(input("Enter constant c: "))
        limit = int(input("Enter the integer search limit: "))
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return

    if limit < 0:
        print("Search limit cannot be negative.")
        return

    solutions = []

    print("\nSearching for Integer Solutions :")

    for x in range(-limit, limit + 1):
        for y in range(-limit, limit + 1):
            if a * x + b * y == c:
                solutions.append((x, y))

    print("\nResults :")
    print("Equation:", a, "x +", b, "y =", c)
    print("Search Range:", -limit, "to", limit)

    if solutions:
        for index, pair in enumerate(solutions, start=1):
            print(
                "Solution", index,
                ": x =", pair[0],
                ", y =", pair[1]
            )
    else:
        print("No integer solutions found within the given range.")

    print("\nTotal Integer Solution Pairs:", len(solutions))

    if len(solutions) == 0:
        print("No solutions exist within the selected search range.")
    elif len(solutions) == 1:
        print("Exactly one integer solution pair was found.")
    else:
        print("Multiple integer solution pairs were found.")

    print("\nVerification :")

    for x, y in solutions:
        result = a * x + b * y
        print(
            "(", x, ",", y, ") =>",
            a, "*", x, "+", b, "*", y, "=",
            result
        )

integersolutioncounter()