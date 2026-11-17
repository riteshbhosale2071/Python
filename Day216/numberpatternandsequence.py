def numberpatternandsequence():
    print("Number Pattern and Sequence Analyzer")

    n = int(input("Enter the number of sequence elements: "))

    if n <= 0:
        print("Please enter a positive number of elements.")
        return

    sequence = []

    for i in range(n):
        value = float(input(f"Enter element {i + 1}: "))
        sequence.append(value)

    print("\nSequence:", sequence)

    if n > 1:
        differences = [
            sequence[i + 1] - sequence[i]
            for i in range(n - 1)
        ]

        print("Differences:", differences)

        if all(value == differences[0] for value in differences):
            print("Pattern: Arithmetic Progression")
            print("Common Difference:", differences[0])

        elif all(sequence[i] != 0 for i in range(n - 1)) and all(
            sequence[i + 1] / sequence[i] == sequence[1] / sequence[0]
            for i in range(1, n - 1)
        ):
            print("Pattern: Geometric Progression")
            print("Common Ratio:", sequence[1] / sequence[0])

        elif all(sequence[i] == sequence[0] for i in range(n)):
            print("Pattern: Constant Sequence")

        else:
            print("Pattern: No simple AP or GP pattern detected.")

    print("\nSequence Analysis:")
    print("Number of Elements:", n)
    print("First Element:", sequence[0])
    print("Last Element:", sequence[-1])
    print("Sum:", sum(sequence))
    print("Average:", sum(sequence) / n)
    print("Minimum:", min(sequence))
    print("Maximum:", max(sequence))

numberpatternandsequence()