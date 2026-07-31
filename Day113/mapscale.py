def mapscale():
    map_distance = float(input("Enter the map distance (cm): "))
    scale = float(input("Enter the scale (e.g., 50000 for 1:50000): "))

    actual_distance_cm = map_distance * scale
    actual_distance_km = actual_distance_cm / 100000

    print("Actual Distance:")
    print(actual_distance_cm, "cm")
    print(actual_distance_km, "km")

mapscale()