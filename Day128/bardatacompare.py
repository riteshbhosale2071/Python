def bardatacomparison():
    categories = input("Enter categories separated by spaces: ").split()
    values = list(map(float, input("Enter bar values separated by spaces: ").split()))

    if len(categories) != len(values):
        print("Number of categories and values must be equal.")
        return

    if len(values) < 2:
        print("Enter at least two bar values.")
        return

    print("\nBar Data Comparison:")

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                result = "greater than"
            elif values[i] < values[j]:
                result = "less than"
            else:
                result = "equal to"

            print(f"{categories[i]} ({values[i]}) is {result} "
                  f"{categories[j]} ({values[j]})")

bardatacomparison()