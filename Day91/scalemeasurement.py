def scalemeasurement():
    start = float(input("Enter start reading (cm): "))
    end = float(input("Enter end reading (cm): "))

    length = end - start

    print("Start Reading:", start, "cm")
    print("End Reading:", end, "cm")
    print("Measured Length:", length, "cm")

scalemeasurement()