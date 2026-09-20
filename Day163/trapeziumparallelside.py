def trapeziumparallelside():
    print("Trapezium Parallel-Side Detector :")

    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    side3 = float(input("Enter length of side 3: "))
    side4 = float(input("Enter length of side 4: "))

    if side1 > 0 and side2 > 0 and side3 > 0 and side4 > 0:
        parallel_pair = input("Are side 1 and side 3 parallel? (yes/no): ")

        if parallel_pair == "yes":
            print("Side 1 and side 3 are parallel.")
            print("The quadrilateral has one pair of parallel sides.")
            print("The shape may be a trapezium.")
        else:
            parallel_pair = input("Are side 2 and side 4 parallel? (yes/no): ")

            if parallel_pair == "yes":
                print("Side 2 and side 4 are parallel.")
                print("The quadrilateral has one pair of parallel sides.")
                print("The shape may be a trapezium.")
            else:
                print("No parallel sides were detected.")
                print("The shape is not a trapezium based on the given information.")
    else:
        print("All side lengths must be greater than zero.")

trapeziumparallelside()