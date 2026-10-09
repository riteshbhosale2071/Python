def depreciationthresholdfinder():
    print("Depreciation Threshold Finder :")

    initial_value = float(input("Enter initial asset value: "))
    rate = float(input("Enter annual depreciation rate (%): "))
    threshold = float(input("Enter target value threshold: "))

    if initial_value <= 0 or rate <= 0 or rate > 100:
        print("Enter valid asset value and depreciation rate.")
        return

    if threshold < 0 or threshold >= initial_value:
        print("Threshold must be non-negative and less than the initial value.")
        return

    current_value = initial_value
    years = 0

    while current_value > threshold:
        current_value = current_value * (1 - rate / 100)
        years += 1

    print("\nThreshold Result :")
    print("Initial Asset Value:", round(initial_value, 2))
    print("Target Threshold:", round(threshold, 2))
    print("Depreciation Rate:", rate, "%")
    print("Years to Reach Threshold:", years)
    print("Asset Value at Threshold:", round(current_value, 2))

depreciationthresholdfinder()