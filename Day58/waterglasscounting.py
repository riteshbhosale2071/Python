def glass():
    water_litres = int(input("Enter total water (litres): "))

    glass_size = 250  # ml

    total_ml = water_litres * 1000

    glasses = total_ml // glass_size

    print("Total Glasses =", glasses)

glass()