def sequencepatterndetector():
    try:
        numbers = list(map(int, input("Enter sequence numbers separated by spaces: ").split()))

        if len(numbers) < 2:
            print("Enter at least two numbers.")
            return

        differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

        print("\nSequence:", numbers)

        if len(set(differences)) == 1:
            print("Pattern: Arithmetic Sequence")
            print("Common Difference:", differences[0])

            next_term = numbers[-1] + differences[0]
            print("Next Term:", next_term)

        elif len(numbers) >= 3:
            ratios = []

            for i in range(len(numbers) - 1):
                if numbers[i] == 0:
                    ratios = []
                    break
                ratios.append(numbers[i + 1] / numbers[i])

            if ratios and all(abs(r - ratios[0]) < 1e-9 for r in ratios):
                print("Pattern: Geometric Sequence")
                print("Common Ratio:", round(ratios[0], 4))

                next_term = numbers[-1] * ratios[0]
                print("Next Term:", round(next_term, 4))

            elif len(set(differences[1:])) == 1:
                print("Pattern: Quadratic Sequence")
                second_difference = differences[1]
                next_term = numbers[-1] + differences[-1] + second_difference

                print("Second Difference:", second_difference)
                print("Next Term:", next_term)

            else:
                print("Pattern: No common arithmetic, geometric, or quadratic pattern detected.")

        else:
            print("Pattern: Insufficient terms to identify a pattern.")

    except ValueError:
        print("Please enter valid integer values.")

sequencepatterndetector()