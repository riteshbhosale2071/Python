def anglesequence():
    start_angle = float(input("Enter the starting angle: "))
    difference = float(input("Enter the angle difference: "))
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("Number of terms must be positive.")
        return

    print("Angle Sequence:")

    for i in range(terms):
        angle = start_angle + i * difference
        print(f"{angle}°", end=" ")

anglesequence()