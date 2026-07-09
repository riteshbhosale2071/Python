def linemeasurement():
    length = int(input("Enter line length (cm): "))

    print("Line:")
    for i in range(length):
        print("-", end="")
    print()

    print("Length of the line:", length, "cm")

linemeasurement()