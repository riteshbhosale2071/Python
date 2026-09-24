def meanfromfrequencytable():
    print("Mean from Frequency Table :")

    number_of_values = int(input("Enter the number of values: "))

    total_frequency = 0
    total_product = 0

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        frequency = int(input("Enter frequency of value " + str(i + 1) + ": "))

        total_product += value * frequency
        total_frequency += frequency

    if total_frequency == 0:
        print("Total frequency cannot be zero.")
        return

    mean = total_product / total_frequency

    print("\nTotal Frequency:", total_frequency)
    print("Sum of Value × Frequency:", total_product)
    print("Mean:", round(mean, 2))

meanfromfrequencytable()