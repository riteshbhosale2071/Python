def milk():
    bottles = int(input("Enter number of bottles: "))
    capacity = int(input("Enter capacity of each bottle (ml): "))

    total_capacity = bottles * capacity

    print("Total Capacity =", total_capacity, "ml")

milk()