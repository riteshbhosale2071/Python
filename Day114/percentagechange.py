def percentagechange():
    old_value = float(input("Enter the old value: "))
    new_value = float(input("Enter the new value: "))

    change = new_value - old_value
    percentage = (change / old_value) * 100

    if change > 0:
        print("Increase:", round(percentage, 2), "%")
    elif change < 0:
        print("Decrease:", round(abs(percentage), 2), "%")
    else:
        print("No Percentage Change")

percentagechange()