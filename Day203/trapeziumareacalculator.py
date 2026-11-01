def trapeziumareacalculator():
    parallel_side_a = float(input("Enter length of first parallel side: "))
    parallel_side_b = float(input("Enter length of second parallel side: "))
    height = float(input("Enter perpendicular height: "))

    if parallel_side_a <= 0 or parallel_side_b <= 0 or height <= 0:
        print("Invalid measurements. All values must be positive.")
        return

    area = 0.5 * (parallel_side_a + parallel_side_b) * height

    print("\nTrapezium Measurement Report")
    print(f"First parallel side: {parallel_side_a:.2f}")
    print(f"Second parallel side: {parallel_side_b:.2f}")
    print(f"Height: {height:.2f}")
    print(f"Area: {area:.2f} square units")

trapeziumareacalculator()