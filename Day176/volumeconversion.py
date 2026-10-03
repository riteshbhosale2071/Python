def volumeconversion():
    print("Volume Conversion Program :")

    volume = float(input("Enter volume: "))

    if volume < 0:
        print("Volume cannot be negative.")
        return

    print("\nChoose the input unit:")
    print("1. Cubic Meter (m³)")
    print("2. Liter (L)")
    print("3. Cubic Centimeter (cm³)")
    print("4. Milliliter (mL)")
    print("5. Cubic Foot (ft³)")

    choice = int(input("Enter choice: "))

    if choice == 1:
        cubic_meter = volume
    elif choice == 2:
        cubic_meter = volume / 1000
    elif choice == 3:
        cubic_meter = volume / 1000000
    elif choice == 4:
        cubic_meter = volume / 1000000000
    elif choice == 5:
        cubic_meter = volume * 0.0283168
    else:
        print("Invalid choice.")
        return

    liter = cubic_meter * 1000
    cubic_centimeter = cubic_meter * 1000000
    milliliter = cubic_meter * 1000000000
    cubic_foot = cubic_meter / 0.0283168

    print("\nConverted Volume :")
    print("Cubic Meter:", round(cubic_meter, 6), "m³")
    print("Liter:", round(liter, 6), "L")
    print("Cubic Centimeter:", round(cubic_centimeter, 6), "cm³")
    print("Milliliter:", round(milliliter, 6), "mL")
    print("Cubic Foot:", round(cubic_foot, 6), "ft³")

volumeconversion()