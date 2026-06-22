def error():
    actual = float(input("Enter the actual value: "))
    measured = float(input("Enter the measured value: "))

    measured_error = abs(actual - measured)

    print("Measured Error is",measured_error)

error()