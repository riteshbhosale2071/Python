def timecomparison():
    print("Time Comparison :")

    hours1 = int(input("Enter first time - hours: "))
    minutes1 = int(input("Enter first time - minutes: "))

    hours2 = int(input("Enter second time - hours: "))
    minutes2 = int(input("Enter second time - minutes: "))

    if hours1 < 0 or minutes1 < 0 or hours2 < 0 or minutes2 < 0:
        print("Enter valid time values.")
        return

    if minutes1 >= 60 or minutes2 >= 60:
        print("Minutes must be between 0 and 59.")
        return

    total1 = hours1 * 60 + minutes1
    total2 = hours2 * 60 + minutes2

    difference = abs(total1 - total2)

    print("\nComparison Result :")

    if total1 > total2:
        print("First time is later.")
    elif total2 > total1:
        print("Second time is later.")
    else:
        print("Both times are equal.")

    print("First Time:", hours1, "hours", minutes1, "minutes")
    print("Second Time:", hours2, "hours", minutes2, "minutes")
    print("Time Difference:", difference, "minutes")

timecomparison()