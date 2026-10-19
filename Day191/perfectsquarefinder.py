def perfectsquarefinder():
    print("Perfect Square Finder :")

    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    if start > end:
        print("Starting number cannot be greater than ending number.")
        return

    if end < 0:
        print("There are no perfect squares in the given range.")
        return

    perfect_squares = []

    for number in range(max(0, start), end + 1):
        root = int(number ** 0.5)

        if root * root == number:
            perfect_squares.append(number)

    print("\nPerfect Square Results :")
    print("Range:", start, "to", end)
    print("Perfect Squares:", perfect_squares)
    print("Total Perfect Squares:", len(perfect_squares))

    print("\nSquare Root Analysis :")

    for number in perfect_squares:
        root = int(number ** 0.5)
        print(number, "=", root, "×", root)

    if len(perfect_squares) == 0:
        print("No perfect squares were found in this range.")
    else:
        print("Smallest Perfect Square:", perfect_squares[0])
        print("Largest Perfect Square:", perfect_squares[-1])

perfectsquarefinder()