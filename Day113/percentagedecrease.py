def percentagedecrease():
    original = float(input("Enter the original value: "))
    new = float(input("Enter the new value: "))

    decrease = original - new
    percentage = (decrease / original) * 100

    print("Decrease:", decrease)
    print("Percentage Decrease:", round(percentage, 2), "%")

percentagedecrease()