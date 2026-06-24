def remaining():
    total_water = float(input("Enter total water (liters): "))
    
    used_water = float(input("Enter water used (liters): "))

    remaining = total_water - used_water

    print("Remaining Water =", remaining, "liters")

remaining()