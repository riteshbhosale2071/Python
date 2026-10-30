def triangleangleclassifier():
    print("Triangle Angle Classifier")

    a = float(input("Enter first angle: "))
    b = float(input("Enter second angle: "))
    c = float(input("Enter third angle: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid angles. All angles must be positive.")

    elif abs(a + b + c - 180) > 0.000001:
        print("Invalid triangle. Sum of angles must be 180 degrees.")

    elif a == 90 or b == 90 or c == 90:
        print("Right-Angled Triangle")

    elif a > 90 or b > 90 or c > 90:
        print("Obtuse-Angled Triangle")

    else:
        print("Acute-Angled Triangle")

triangleangleclassifier()