def growthrateranking():
    print("Growth Rate Ranking :")

    count = int(input("Enter number of items to compare: "))

    if count <= 0:
        print("Enter a valid number of items.")
        return

    items = []

    for i in range(count):
        name = input("Enter item name: ")
        initial_value = float(input("Enter initial value: "))
        final_value = float(input("Enter final value: "))

        if initial_value <= 0:
            print("Initial value must be greater than zero.")
            return

        growth_rate = ((final_value - initial_value) / initial_value) * 100
        items.append([name, growth_rate])

    items.sort(key=lambda item: item[1], reverse=True)

    print("\nGrowth Rate Ranking :")

    for i in range(len(items)):
        print(i + 1, ".", items[i][0], "-",
              round(items[i][1], 2), "%")

growthrateranking()