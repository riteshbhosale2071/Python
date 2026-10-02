def cuboidvolumefromcapacity():
    print("Cuboid Volume from Capacity :")

    capacity = float(input("Enter capacity in liters: "))

    if capacity <= 0:
        print("Capacity must be greater than zero.")
        return

    volume_cm3 = capacity * 1000
    volume_m3 = capacity / 1000

    print("\nCapacity:", capacity, "liters")
    print("Volume in Cubic Centimeters:", round(volume_cm3, 2), "cm³")
    print("Volume in Cubic Meters:", round(volume_m3, 4), "m³")

cuboidvolumefromcapacity()