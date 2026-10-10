def areabudget():
    print("Area Budget :")

    print("1. Floor Tiling")
    print("2. Wall Painting")
    print("3. Land Fencing and Cost")
    print("4. Garden Development")

    choice = int(input("Select a project: "))

    if choice == 1:
        length = float(input("Enter floor length: "))
        width = float(input("Enter floor width: "))
        cost_per_unit = float(input("Enter tiling cost per square unit: "))

        if length <= 0 or width <= 0 or cost_per_unit < 0:
            print("Enter valid values.")
            return

        area = length * width
        total_cost = area * cost_per_unit

    elif choice == 2:
        length = float(input("Enter wall length: "))
        height = float(input("Enter wall height: "))
        cost_per_unit = float(input("Enter painting cost per square unit: "))

        if length <= 0 or height <= 0 or cost_per_unit < 0:
            print("Enter valid values.")
            return

        area = length * height
        total_cost = area * cost_per_unit

    elif choice == 3:
        length = float(input("Enter land length: "))
        width = float(input("Enter land width: "))
        fencing_cost = float(input("Enter fencing cost per unit length: "))

        if length <= 0 or width <= 0 or fencing_cost < 0:
            print("Enter valid values.")
            return

        area = length * width
        perimeter = 2 * (length + width)
        total_cost = perimeter * fencing_cost

        print("Land Perimeter:", round(perimeter, 2))

    elif choice == 4:
        length = float(input("Enter garden length: "))
        width = float(input("Enter garden width: "))
        cost_per_unit = float(input("Enter development cost per square unit: "))

        if length <= 0 or width <= 0 or cost_per_unit < 0:
            print("Enter valid values.")
            return

        area = length * width
        total_cost = area * cost_per_unit

    else:
        print("Invalid choice.")
        return

    print("\nBudget Summary :")
    print("Total Area:", round(area, 2))
    print("Estimated Total Cost:", round(total_cost, 2))

    budget = float(input("Enter your available budget: "))

    if budget < 0:
        print("Budget cannot be negative.")
        return

    if total_cost > budget:
        print("Budget Exceeded By:", round(total_cost - budget, 2))
    elif total_cost < budget:
        print("Remaining Budget:", round(budget - total_cost, 2))
    else:
        print("The project exactly matches your budget.")

areabudget()