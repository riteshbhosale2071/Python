def intersectingchords():
    print("Intersecting Chords Calculator")
    print("1. Find Missing Segment")
    print("2. Verify Intersecting Chords Theorem")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        a = float(input("Enter first segment length: "))
        b = float(input("Enter second segment length: "))
        c = float(input("Enter third segment length: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Segment lengths must be positive.")
            return

        d = (a * b) / c
        print("Missing Segment Length =", round(d, 2))

    elif choice == "2":
        a = float(input("Enter first segment length (a): "))
        b = float(input("Enter second segment length (b): "))
        c = float(input("Enter third segment length (c): "))
        d = float(input("Enter fourth segment length (d): "))

        if min(a, b, c, d) <= 0:
            print("All segment lengths must be positive.")
            return

        product1 = a * b
        product2 = c * d

        print("First Product =", round(product1, 2))
        print("Second Product =", round(product2, 2))

        if abs(product1 - product2) < 1e-9:
            print("The intersecting chords theorem is verified.")
        else:
            print("The intersecting chords theorem is not verified.")

    else:
        print("Invalid choice.")

intersectingchords()