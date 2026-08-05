def circlearc():
    radius = float(input("Enter the radius of the circle: "))
    angle = float(input("Enter the central angle (in degrees): "))

    print("\nCircle Arc Construction Steps:")
    print("1. Draw a circle with radius", radius)
    print("2. Mark the center of the circle.")
    print("3. Draw one radius from the center.")
    print("4. Measure", angle, "degrees from the first radius.")
    print("5. Draw the second radius.")
    print("6. The curved part between the two radii is the required arc.")

circlearc()