def gardenfencingcost():
    length = float(input("Enter the garden length: "))
    width = float(input("Enter the garden width: "))
    cost_per_meter = float(input("Enter fencing cost per meter: "))

    if length <= 0 or width <= 0 or cost_per_meter < 0:
        print("Enter valid positive dimensions and a non-negative cost.")
        return

    perimeter = 2 * (length + width)
    total_cost = perimeter * cost_per_meter

    print("Garden Perimeter:", perimeter, "meters")
    print("Total Fencing Cost:", total_cost)

gardenfencingcost()