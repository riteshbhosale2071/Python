def meanreplacement():
    print("Mean Replacement :")

    n = int(input("Enter the number of observations: "))

    if n <= 0:
        print("Number of observations must be greater than zero.")
        return

    numbers = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        numbers.append(value)

    original_mean = sum(numbers) / n

    print("\nOriginal Dataset:", numbers)
    print("Original Mean:", round(original_mean, 2))

    old_value = float(input("\nEnter the value to replace: "))

    if old_value not in numbers:
        print("The value is not present in the dataset.")
        return

    new_value = float(input("Enter the replacement value: "))

    index = numbers.index(old_value)
    numbers[index] = new_value

    new_mean = sum(numbers) / n
    mean_change = new_mean - original_mean

    print("\nReplacement Analysis :")
    print("Updated Dataset:", numbers)
    print("Original Mean:", round(original_mean, 2))
    print("Updated Mean:", round(new_mean, 2))
    print("Mean Change:", round(mean_change, 2))

    if new_mean > original_mean:
        print("Result: The mean increased.")
    elif new_mean < original_mean:
        print("Result: The mean decreased.")
    else:
        print("Result: The mean remained unchanged.")

    print("Original Total:", round(original_mean * n, 2))
    print("Updated Total:", round(new_mean * n, 2))

meanreplacement()