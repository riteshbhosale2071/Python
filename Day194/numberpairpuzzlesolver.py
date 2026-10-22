def numberpairpuzzlesolver():
    print("Number Pair Puzzle Solver :")
    print("Find pairs of numbers that satisfy given conditions.")

    try:
        target_sum = int(input("Enter the required sum: "))
        target_product = int(input("Enter the required product: "))
        lower_limit = int(input("Enter the minimum number: "))
        upper_limit = int(input("Enter the maximum number: "))
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return

    if lower_limit > upper_limit:
        print("Minimum number cannot exceed maximum number.")
        return

    solutions = []

    for first in range(lower_limit, upper_limit + 1):
        for second in range(first, upper_limit + 1):
            if first + second == target_sum and first * second == target_product:
                solutions.append((first, second))

    print("\nPuzzle Conditions :")
    print("Required Sum:", target_sum)
    print("Required Product:", target_product)
    print("Number Range:", lower_limit, "to", upper_limit)

    print("\nSolution Pairs :")

    if solutions:
        for index, pair in enumerate(solutions, start=1):
            first, second = pair

            print("\nSolution", index)
            print("First Number:", first)
            print("Second Number:", second)
            print("Sum:", first + second)
            print("Product:", first * second)

        print("\nTotal Solution Pairs:", len(solutions))
    else:
        print("No number pairs satisfy both conditions.")

    print("\nVerification :")

    for first, second in solutions:
        sum_valid = first + second == target_sum
        product_valid = first * second == target_product

        print(
            "Pair:", (first, second),
            "| Sum Valid:", sum_valid,
            "| Product Valid:", product_valid
        )

    if len(solutions) == 1:
        print("\nThe puzzle has exactly one solution pair.")
    elif len(solutions) > 1:
        print("\nThe puzzle has multiple solution pairs.")
    else:
        print("\nThe puzzle has no solution in the given range.")

numberpairpuzzlesolver()