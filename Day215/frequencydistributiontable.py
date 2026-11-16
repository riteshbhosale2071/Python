def frequencydistributiontable():
    print("Frequency Distribution Table Generator")

    n = int(input("Enter the number of data values: "))

    if n <= 0:
        print("Please enter a positive number of values.")
        return

    data = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))
        data.append(value)

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    print("\nFrequency Distribution Table :")
    print(f"{'Value':<15}{'Frequency':<15}{'Percentage':<15}")
    print("-" * 45)

    for value in sorted(frequency):
        count = frequency[value]
        percentage = (count / n) * 100
        print(f"{value:<15g}{count:<15}{percentage:.2f}%")

    print("-" * 45)
    print(f"{'Total':<15}{n:<15}{100:.2f}%")

    print("\nTotal Unique Values:", len(frequency))
    print("Minimum Value:", min(data))
    print("Maximum Value:", max(data))
    print("Mean:", sum(data) / n)

frequencydistributiontable()