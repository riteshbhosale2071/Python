def percentagecomparison():
    percentage1 = float(input("Enter the first percentage: "))
    percentage2 = float(input("Enter the second percentage: "))

    print("First Percentage:", percentage1, "%")
    print("Second Percentage:", percentage2, "%")

    if percentage1 > percentage2:
        print("First percentage is greater.")
    elif percentage2 > percentage1:
        print("Second percentage is greater.")
    else:
        print("Both percentages are equal.")

percentagecomparison()