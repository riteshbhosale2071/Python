def categorywinner():
    categories = input("Enter category names separated by spaces: ").split()
    values = list(map(float, input("Enter values separated by spaces: ").split()))

    if len(categories) != len(values):
        print("Number of categories and values must be equal.")
        return

    if not categories:
        print("Please enter at least one category.")
        return

    highest = max(values)

    winners = [
        categories[i]
        for i in range(len(categories))
        if values[i] == highest
    ]

    print("Highest Value:", highest)
    print("Category Winner(s):", ", ".join(winners))

categorywinner()