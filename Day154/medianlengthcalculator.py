def medianlengthcalculator():
    print("Median Length Calculator :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    median_a = ((2 * b * b + 2 * c * c - a * a) / 4) ** 0.5
    median_b = ((2 * a * a + 2 * c * c - b * b) / 4) ** 0.5
    median_c = ((2 * a * a + 2 * b * b - c * c) / 4) ** 0.5

    print("\nMedian Lengths :")
    print("Median to side a: {:.2f}".format(median_a))
    print("Median to side b: {:.2f}".format(median_b))
    print("Median to side c: {:.2f}".format(median_c))

medianlengthcalculator()