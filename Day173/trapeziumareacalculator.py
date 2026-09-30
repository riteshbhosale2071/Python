def trapeziumareacalculator():
    print("Trapezium Area Calculator :")

    first_parallel_side = float(input("Enter first parallel side: "))
    second_parallel_side = float(input("Enter second parallel side: "))
    height = float(input("Enter height: "))

    if first_parallel_side <= 0 or second_parallel_side <= 0 or height <= 0:
        print("All measurements must be greater than zero.")
        return

    area = 0.5 * (first_parallel_side + second_parallel_side) * height

    print("\nFirst Parallel Side:", first_parallel_side)
    print("Second Parallel Side:", second_parallel_side)
    print("Height:", height)
    print("Area of Trapezium:", round(area, 2))

trapeziumareacalculator()