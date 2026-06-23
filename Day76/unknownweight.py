def unknown():
    totalweight = float(input("Enter the total weight (kg): "))
    knownweight = float(input("Enter the known weight (kg): "))

    unknownweight = totalweight - knownweight

    print("Unknown Weight is",unknownweight,"kg")

unknown()