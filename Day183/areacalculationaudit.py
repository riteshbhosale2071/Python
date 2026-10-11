def areacalculationaudit():
    print("Area Calculation Audit :")

    number = int(input("Enter the number of calculations to audit: "))

    if number <= 0:
        print("Number of calculations must be greater than zero.")
        return

    passed = 0
    failed = 0
    total_area = 0

    for i in range(number):
        print("\nCalculation", i + 1)
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")

        choice = input("Select shape (1-4): ")

        if choice == "1":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            entered_area = float(input("Enter your calculated area: "))

            if length <= 0 or width <= 0:
                print("Invalid dimensions.")
                failed += 1
                continue

            correct_area = length * width

        elif choice == "2":
            side = float(input("Enter side length: "))
            entered_area = float(input("Enter your calculated area: "))

            if side <= 0:
                print("Invalid side length.")
                failed += 1
                continue

            correct_area = side * side

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            entered_area = float(input("Enter your calculated area: "))

            if base <= 0 or height <= 0:
                print("Invalid dimensions.")
                failed += 1
                continue

            correct_area = 0.5 * base * height

        elif choice == "4":
            radius = float(input("Enter radius: "))
            entered_area = float(input("Enter your calculated area: "))

            if radius <= 0:
                print("Invalid radius.")
                failed += 1
                continue

            correct_area = 3.14159 * radius * radius

        else:
            print("Invalid shape selection.")
            failed += 1
            continue

        difference = abs(entered_area - correct_area)

        print("Expected Area:", round(correct_area, 2))
        print("Entered Area:", round(entered_area, 2))
        print("Difference:", round(difference, 2))

        if difference < 0.01:
            print("Audit Status: PASSED")
            passed += 1
            total_area += correct_area
        else:
            print("Audit Status: FAILED")
            failed += 1

    print("\nFinal Audit Report :")
    print("Total Calculations:", number)
    print("Passed Audits:", passed)
    print("Failed Audits:", failed)
    print("Total Area of Passed Calculations:", round(total_area, 2))

    if failed == 0:
        print("Overall Status: All calculations passed.")
    else:
        print("Overall Status: Some calculations require correction.")

areacalculationaudit()