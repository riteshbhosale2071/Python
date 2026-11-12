def arithmeticprogressionchecker():
    try:
        numbers = list(map(float, input("Enter sequence numbers separated by spaces: ").split()))

        if len(numbers) < 2:
            print("Enter at least two numbers.")
            return

        differences = [
            numbers[i + 1] - numbers[i]
            for i in range(len(numbers) - 1)
        ]

        print("Sequence:", numbers)
        print("Common Differences:", differences)

        if all(abs(d - differences[0]) < 1e-9 for d in differences):
            print("Result: The sequence is an Arithmetic Progression.")
            print("Common Difference:", differences[0])

            next_term = numbers[-1] + differences[0]
            print("Next Term:", next_term)
        else:
            print("Result: The sequence is not an Arithmetic Progression.")

    except ValueError:
        print("Please enter valid numeric values.")

arithmeticprogressionchecker()