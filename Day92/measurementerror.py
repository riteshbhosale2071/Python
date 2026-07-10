def measurementerror():
    actual = float(input("Enter actual measurement (cm): "))
    measured = float(input("Enter measured value (cm): "))

    error = abs(actual - measured)

    print("Measurement Error:", error, "cm")

    if error == 0:
        print("No Error")
    else:
        print("Measurement Error Detected")

measurementerror()