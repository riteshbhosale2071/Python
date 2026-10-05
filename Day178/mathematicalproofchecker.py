def mathematicalproofchecker():
    print("Mathematical Proof Checker :")
    print("1. Even Number Proof")
    print("2. Odd Number Proof")
    print("3. Triangle Angle Sum Proof")
    print("4. Pythagorean Theorem Check")
    print("5. Arithmetic Sequence Check")

    choice = int(input("Select a proof type: "))

    if choice == 1:
        number = int(input("Enter an integer: "))

        if number % 2 == 0:
            print("\nProof:")
            print(number, "is divisible by 2.")
            print("Therefore,", number, "is an even number.")
        else:
            print("\nThe given number is not even.")

    elif choice == 2:
        number = int(input("Enter an integer: "))

        if number % 2 != 0:
            print("\nProof:")
            print(number, "is not divisible by 2.")
            print("Therefore,", number, "is an odd number.")
        else:
            print("\nThe given number is not odd.")

    elif choice == 3:
        angle1 = float(input("Enter first angle: "))
        angle2 = float(input("Enter second angle: "))
        angle3 = float(input("Enter third angle: "))

        total = angle1 + angle2 + angle3

        print("\nProof:")
        print("Angle Sum:", round(total, 2), "degrees")

        if abs(total - 180) < 0.000001:
            print("Proof Verified: The triangle angle sum is 180 degrees.")
        else:
            print("Proof Failed: The angles do not sum to 180 degrees.")

    elif choice == 4:
        a = float(input("Enter first perpendicular side: "))
        b = float(input("Enter second perpendicular side: "))
        c = float(input("Enter hypotenuse: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("All sides must be greater than zero.")
            return

        left_side = a ** 2 + b ** 2
        right_side = c ** 2

        print("\nProof:")
        print("a² + b² =", round(left_side, 2))
        print("c² =", round(right_side, 2))

        if abs(left_side - right_side) < 0.000001:
            print("Proof Verified: The Pythagorean relationship holds.")
        else:
            print("Proof Failed: The Pythagorean relationship does not hold.")

    elif choice == 5:
        first = float(input("Enter first term: "))
        second = float(input("Enter second term: "))
        third = float(input("Enter third term: "))

        difference1 = second - first
        difference2 = third - second

        print("\nProof:")
        print("First Difference:", round(difference1, 2))
        print("Second Difference:", round(difference2, 2))

        if abs(difference1 - difference2) < 0.000001:
            print("Proof Verified: The three terms follow an arithmetic pattern.")
        else:
            print("Proof Failed: The three terms do not form an arithmetic sequence.")

    else:
        print("Invalid proof type.")

mathematicalproofchecker()