def draw():
    radius = int(input("Enter the radius of the circle: "))

    print("\nCircle Simulation")
    print("-" * 30)

    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if i * i + j * j <= radius * radius:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

draw()