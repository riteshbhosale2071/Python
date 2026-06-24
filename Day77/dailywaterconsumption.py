def consumption():
    glasses = int(input("Enter number of glasses of water consumed: "))

    water_per_glass = 250

    total_water = glasses * water_per_glass

    print("Total Water Consumed =", total_water, "ml")
    print("Total Water Consumed =", total_water / 1000, "liters")

consumption()