def factorisationsequenceanalyzer():
    print("=== Factorisation Sequence Analyzer ===")

    n = int(input("Enter number of terms: "))

    numbers = []

    for i in range(n):
        number = int(input("Enter number " + str(i + 1) + ": "))
        numbers.append(number)

    print("Factorisation of each number:")

    for number in numbers:
        print("Number:", number)
        factors = []

        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)

        print("Factors:", factors)

    print("Common factors:")

    common_count = 0

    for i in range(1, min(numbers) + 1):
        found = True

        for number in numbers:
            if number % i != 0:
                found = False
                break

        if found:
            print(i)
            common_count += 1

    if common_count == 0:
        print("No common factors found.")

factorisationsequenceanalyzer()