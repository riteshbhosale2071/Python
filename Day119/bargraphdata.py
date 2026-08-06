def bargraphdata():
    categories = []
    values = []

    n = int(input("Enter the number of categories: "))

    for i in range(n):
        category = input(f"Enter category {i + 1}: ")
        value = float(input(f"Enter value for {category}: "))
        categories.append(category)
        values.append(value)

    print("\nBar Graph Data")
    for i in range(n):
        print(categories[i], ":", values[i])

bargraphdata()