def measurementerror():
    actual = float(input("Enter actual measurement: "))
    measured = float(input("Enter measured value: "))
    error = actual - measured

    if error < 0:
        error = -error

    print("Measurement Error =", error)

measurementerror()