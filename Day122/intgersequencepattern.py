def integersequencepattern():
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

    if len(numbers) < 3:
        print("Enter at least 3 integers.")
        return

    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    if len(set(differences)) == 1:
        print("Pattern: Add", differences[0], "to each term.")
    elif all(numbers[i + 1] == numbers[i] * numbers[1] // numbers[0]
             for i in range(len(numbers) - 1)) and numbers[0] != 0:
        print("Pattern: Multiply by", numbers[1] // numbers[0])
    elif all(numbers[i] == -numbers[i - 1] for i in range(1, len(numbers))):
        print("Pattern: Alternate between positive and negative values.")
    else:
        print("Pattern: No simple arithmetic rule detected.")

integersequencepattern()