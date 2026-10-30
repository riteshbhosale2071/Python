def triangletypeclassifier():
    print("Triangle Type Classifier")
    print("1. Classify by sides")
    print("2. Classify by angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Invalid side lengths.")

        elif a + b > c and a + c > b and b + c > a:
            if a == b == c:
                print("Equilateral Triangle")
            elif a == b or b == c or a == c:
                print("Isosceles Triangle")
            else:
                print("Scalene Triangle")
        else:
            print("Invalid Triangle.")

    elif choice == "2":
        a = float(input("Enter first angle: "))
        b = float(input("Enter second angle: "))
        c = float(input("Enter third angle: "))

        if a <= 0 or b <= 0 or c <= 0 or abs(a + b + c - 180) > 0.000001:
            print("Invalid triangle angles.")

        elif a == 90 or b == 90 or c == 90:
            print("Right-Angled Triangle")
        elif a > 90 or b > 90 or c > 90:
            print("Obtuse-Angled Triangle")
        else:
            print("Acute-Angled Triangle")

    else:
        print("Invalid choice.")

triangletypeclassifier()