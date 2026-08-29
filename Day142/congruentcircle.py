def congruentcircle():
    radius1 = float(input("Enter radius of first circle: "))
    radius2 = float(input("Enter radius of second circle: "))

    if radius1 <= 0 or radius2 <= 0:
        print("Radius must be positive.")
        return

    if radius1 == radius2:
        print("The circles are Congruent.")
        print("Both circles have the same radius.")
    else:
        print("The circles are Not Congruent.")

congruentcircle()