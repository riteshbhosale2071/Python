def areaunitconverter():
    print("Area Unit Converter with Validation :")
    print("1. Square Meter")
    print("2. Square Kilometer")
    print("3. Square Foot")
    print("4. Square Inch")
    print("5. Acre")
    print("6. Hectare")

    units = {
        1: ("Square Meter", 1),
        2: ("Square Kilometer", 1000000),
        3: ("Square Foot", 0.092903),
        4: ("Square Inch", 0.00064516),
        5: ("Acre", 4046.8564224),
        6: ("Hectare", 10000)
    }

    source = int(input("Choose source unit (1-6): "))
    target = int(input("Choose target unit (1-6): "))

    if source not in units or target not in units:
        print("Invalid unit selection. Please choose between 1 and 6.")
        return

    area = float(input("Enter area value: "))

    if area < 0:
        print("Invalid area. Area cannot be negative.")
        return

    source_name, source_factor = units[source]
    target_name, target_factor = units[target]

    area_in_square_meters = area * source_factor
    converted_area = area_in_square_meters / target_factor

    print("\nConversion Result :")
    print("Original Area:", area, source_name)
    print("Converted Area:", round(converted_area, 6), target_name)

    if source == target:
        print("Both units are the same. No conversion was required.")

areaunitconverter()