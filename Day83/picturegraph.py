def picturegraph():
    n = int(input("Enter number of categories: "))
    value = int(input("Enter value of one symbol: "))

    pictograph = {}

    for i in range(n):
        category = input(f"Enter category {i+1}: ")
        symbols = int(input(f"Enter number of symbols for {category}: "))
        pictograph[category] = symbols

    print("\nPicture Graph Report")
    print("-" * 35)

    highest_category = ""
    highest_total = 0
    grand_total = 0

    for category, symbols in pictograph.items():
        total = symbols * value
        print(category, ":", "*" * symbols, "=", total)

        grand_total += total

        if total > highest_total:
            highest_total = total
            highest_category = category

    print("\nGrand Total =", grand_total)
    print("Highest Category =", highest_category)
    print("Highest Total =", highest_total)

picturegraph()