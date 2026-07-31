def percentageincrease():
    original = float(input("Enter the original value: "))
    new = float(input("Enter the new value: "))

    increase = new - original
    percentage = (increase / original) * 100

    print("Increase:", increase)
    print("Percentage Increase:", round(percentage, 2), "%")

percentageincrease()