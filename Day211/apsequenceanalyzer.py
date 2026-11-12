def apsequenceanalyzer():
    try:
        numbers = list(map(float, input("Enter AP terms separated by spaces: ").split()))

        if len(numbers) < 2:
            print("Enter at least two terms.")
            return

        differences = [
            numbers[i + 1] - numbers[i]
            for i in range(len(numbers) - 1)
        ]

        print("\nAP Sequence Analysis")
        print("Sequence:", numbers)
        print("Number of Terms:", len(numbers))
        print("First Term:", numbers[0])
        print("Last Term:", numbers[-1])
        print("Differences:", differences)

        if all(abs(d - differences[0]) < 1e-9 for d in differences):
            common_difference = differences[0]
            total_sum = sum(numbers)
            next_term = numbers[-1] + common_difference

            print("\nResult: Valid Arithmetic Progression")
            print("Common Difference:", round(common_difference, 4))
            print("Sum of Terms:", round(total_sum, 4))
            print("Next Term:", round(next_term, 4))
            print("Average Term:", round(total_sum / len(numbers), 4))

            if common_difference > 0:
                print("Pattern: Increasing AP")
            elif common_difference < 0:
                print("Pattern: Decreasing AP")
            else:
                print("Pattern: Constant AP")
        else:
            print("\nResult: Not an Arithmetic Progression")
            print("The differences between consecutive terms are not equal.")

    except ValueError:
        print("Please enter valid numeric terms.")

apsequenceanalyzer()