def measurementreport():
    measure1 = float(input("Enter first measurement (cm): "))
    measure2 = float(input("Enter second measurement (cm): "))

    print("First Measurement :", measure1, "cm")
    print("Second Measurement:", measure2, "cm")

    if measure1 > measure2:
        print("First measurement is greater.")
    elif measure2 > measure1:
        print("Second measurement is greater.")
    else:
        print("Both measurements are equal.")

measurementreport()