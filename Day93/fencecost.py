def fencecost():
    length = float(input("Enter length of the field: "))
    width = float(input("Enter width of the field: "))
    cost_per_unit = float(input("Enter fencing cost per unit length: "))

    perimeter = 2 * (length + width)
    total_cost = perimeter * cost_per_unit

    print("Perimeter:", perimeter)
    print("Total Fence Cost:", total_cost)

fencecost()