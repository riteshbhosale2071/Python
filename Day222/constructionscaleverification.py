def constructionscaleverification():
    print("Construction Scale Verification :")
    print("1. Verify Drawing Scale")
    print("2. Find Actual Length")
    print("3. Find Drawing Length")
    print("4. Find Scale Ratio")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        drawing = float(input("Enter drawing measurement: "))
        actual = float(input("Enter actual measurement: "))

        if drawing <= 0 or actual <= 0:
            print("Measurements must be positive.")
            return

        scale = drawing / actual
        print("Scale Ratio = 1 :", round(actual / drawing, 4))
        print("Scale Factor =", round(scale, 6))

    elif choice == "2":
        drawing = float(input("Enter drawing measurement: "))
        scale = float(input("Enter scale denominator (e.g. 100 for 1:100): "))

        if drawing <= 0 or scale <= 0:
            print("Values must be positive.")
            return

        actual = drawing * scale
        print("Actual Length =", round(actual, 2))

    elif choice == "3":
        actual = float(input("Enter actual measurement: "))
        scale = float(input("Enter scale denominator (e.g. 100 for 1:100): "))

        if actual <= 0 or scale <= 0:
            print("Values must be positive.")
            return

        drawing = actual / scale
        print("Drawing Length =", round(drawing, 2))

    elif choice == "4":
        drawing = float(input("Enter drawing measurement: "))
        actual = float(input("Enter actual measurement: "))

        if drawing <= 0 or actual <= 0:
            print("Measurements must be positive.")
            return

        from math import gcd

        d = round(drawing * 10000)
        a = round(actual * 10000)
        common = gcd(d, a)

        print("Simplified Scale Ratio =", d // common, ":", a // common)

    else:
        print("Invalid choice.")

constructionscaleverification()