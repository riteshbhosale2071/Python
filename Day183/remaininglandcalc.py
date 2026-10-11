def remaininglandcalc():
    print("Remaining Land Calculator :")

    total_length = float(input("Enter total land length: "))
    total_width = float(input("Enter total land width: "))
    used_length = float(input("Enter used land length: "))
    used_width = float(input("Enter used land width: "))

    if total_length <= 0 or total_width <= 0:
        print("Total land dimensions must be greater than zero.")
        return

    if used_length < 0 or used_width < 0:
        print("Used land dimensions cannot be negative.")
        return

    total_area = total_length * total_width
    used_area = used_length * used_width

    if used_area > total_area:
        print("Used land area cannot exceed total land area.")
        return

    remaining_area = total_area - used_area
    used_percentage = (used_area / total_area) * 100
    remaining_percentage = (remaining_area / total_area) * 100

    print("\nLand Area Summary :")
    print("Total Land Area:", round(total_area, 2))
    print("Used Land Area:", round(used_area, 2))
    print("Remaining Land Area:", round(remaining_area, 2))
    print("Used Land Percentage:", round(used_percentage, 2), "%")
    print("Remaining Land Percentage:", round(remaining_percentage, 2), "%")

remaininglandcalc()