def multiroundfencing():
    length = float(input("Enter the length of the rectangular field: "))
    width = float(input("Enter the width of the rectangular field: "))
    rounds = int(input("Enter the number of fencing rounds: "))
    cost_per_meter = float(input("Enter fencing cost per meter: "))

    if length <= 0 or width <= 0 or rounds <= 0 or cost_per_meter < 0:
        print("Enter valid values.")
        return

    perimeter = 2 * (length + width)
    total_length = perimeter * rounds
    total_cost = total_length * cost_per_meter

    print("Perimeter:", perimeter, "meters")
    print("Total Fencing Length:", total_length, "meters")
    print("Total Fencing Cost:", total_cost)

multiroundfencing()