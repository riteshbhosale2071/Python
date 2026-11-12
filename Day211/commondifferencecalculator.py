def commondifferencecalculator():
    try:
        numbers = list(map(float, input("Enter sequence terms separated by spaces: ").split()))

        if len(numbers) < 2:
            print("Enter at least two terms.")
            return

        differences = [
            numbers[i + 1] - numbers[i]
            for i in range(len(numbers) - 1)
        ]

        print("\nSequence:", numbers)
        print("Calculated Differences:", differences)

        if all(abs(d - differences[0]) < 1e-9 for d in differences):
            print("Common Difference:", round(differences[0], 4))
            print("The sequence is an Arithmetic Progression.")
        else:
            print("No common difference found.")
            print("The sequence is not an Arithmetic Progression.")

    except ValueError:
        print("Please enter valid numeric values.")

commondifferencecalculator()