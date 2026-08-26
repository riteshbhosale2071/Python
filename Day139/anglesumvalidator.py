def anglesumvalidator():
    angles = list(map(float, input("Enter angles separated by spaces: ").split()))
    expected_sum = float(input("Enter the required angle sum: "))

    if not angles:
        print("Please enter at least one angle.")
        return

    actual_sum = sum(angles)

    print("Actual Angle Sum:", actual_sum, "°")
    print("Required Angle Sum:", expected_sum, "°")

    if actual_sum == expected_sum:
        print("The angle sum is valid.")
    else:
        print("The angle sum is not valid.")

anglesumvalidator()