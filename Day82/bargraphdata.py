def bargraph():
    n = int(input("Enter number of categories: "))

    categories = []
    values = []

    for i in range(n):
        category = input(f"Enter category {i+1}: ")
        value = int(input(f"Enter value for {category}: "))

        categories.append(category)
        values.append(value)

    print("\nBar Graph Data")
    print("-" * 30)

    for i in range(n):
        print(categories[i], ":", values[i], "*" * values[i])

bargraph()