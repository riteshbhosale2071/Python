def mathformulaselection():
    print("Math Formula Selection :")
    print("1. Circle Area")
    print("2. Circle Circumference")
    print("3. Triangle Area")
    print("4. Rectangle Area")
    print("5. Rectangle Perimeter")
    print("6. Simple Interest")
    print("7. Compound Interest")
    print("8. Speed")
    print("9. Distance")
    print("10. Average")

    choice = int(input("\nSelect a formula: "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        if radius > 0:
            result = 3.14159 * radius ** 2
            print("Formula: π × r²")
            print("Result:", round(result, 2))
        else:
            print("Radius must be greater than zero.")

    elif choice == 2:
        radius = float(input("Enter radius: "))
        if radius > 0:
            result = 2 * 3.14159 * radius
            print("Formula: 2 × π × r")
            print("Result:", round(result, 2))
        else:
            print("Radius must be greater than zero.")

    elif choice == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        if base > 0 and height > 0:
            result = 0.5 * base * height
            print("Formula: ½ × base × height")
            print("Result:", round(result, 2))
        else:
            print("Values must be greater than zero.")

    elif choice == 4:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        if length > 0 and width > 0:
            result = length * width
            print("Formula: length × width")
            print("Result:", round(result, 2))
        else:
            print("Values must be greater than zero.")

    elif choice == 5:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        if length > 0 and width > 0:
            result = 2 * (length + width)
            print("Formula: 2 × (length + width)")
            print("Result:", round(result, 2))
        else:
            print("Values must be greater than zero.")

    elif choice == 6:
        principal = float(input("Enter principal: "))
        rate = float(input("Enter rate: "))
        time = float(input("Enter time: "))
        if principal > 0 and rate >= 0 and time > 0:
            result = (principal * rate * time) / 100
            print("Formula: (P × R × T) / 100")
            print("Simple Interest:", round(result, 2))
        else:
            print("Enter valid values.")

    elif choice == 7:
        principal = float(input("Enter principal: "))
        rate = float(input("Enter annual rate: "))
        time = float(input("Enter time in years: "))
        if principal > 0 and rate >= 0 and time > 0:
            amount = principal * (1 + rate / 100) ** time
            interest = amount - principal
            print("Formula: P × (1 + R/100)ᵀ")
            print("Amount:", round(amount, 2))
            print("Compound Interest:", round(interest, 2))
        else:
            print("Enter valid values.")

    elif choice == 8:
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        if distance >= 0 and time > 0:
            result = distance / time
            print("Formula: Distance / Time")
            print("Speed:", round(result, 2))
        else:
            print("Enter valid values.")

    elif choice == 9:
        speed = float(input("Enter speed: "))
        time = float(input("Enter time: "))
        if speed >= 0 and time >= 0:
            result = speed * time
            print("Formula: Speed × Time")
            print("Distance:", round(result, 2))
        else:
            print("Enter valid values.")

    elif choice == 10:
        number_of_values = int(input("Enter number of values: "))

        if number_of_values <= 0:
            print("Enter a valid number of values.")
            return

        total = 0

        for i in range(number_of_values):
            value = float(input("Enter value " + str(i + 1) + ": "))
            total += value

        result = total / number_of_values

        print("Formula: Sum of values / Number of values")
        print("Average:", round(result, 2))

    else:
        print("Invalid formula selection.")

mathformulaselection()