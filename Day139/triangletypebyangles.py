def triangletypebyangles():
    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))
    angle3 = float(input("Enter third angle: "))

    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        print("Angles must be positive.")
        return

    if abs(angle1 + angle2 + angle3 - 180) > 1e-9:
        print("Invalid triangle. Angles must add up to 180°.")
        return

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Triangle Type: Right-Angled Triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Triangle Type: Obtuse-Angled Triangle")
    else:
        print("Triangle Type: Acute-Angled Triangle")

triangletypebyangles()