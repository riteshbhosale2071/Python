def linearpair():
    angle1 = float(input("Enter the first angle in degrees: "))
    angle2 = float(input("Enter the second angle in degrees: "))

    if angle1 <= 0 or angle2 <= 0:
        print("Angles must be positive.")
    elif angle1 + angle2 == 180:
        print("The angles form a Linear Pair.")
    else:
        print("The angles do not form a Linear Pair.")

linearpair()