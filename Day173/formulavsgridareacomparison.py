def formulavsgridareacomparison():
    print("Formula-vs-Grid Area Comparison :")

    print("\nEnter rectangle dimensions:")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    if length <= 0 or width <= 0:
        print("Length and width must be greater than zero.")
        return

    formula_area = length * width

    print("\nEnter grid details:")
    cell_area = float(input("Enter area of one grid cell: "))
    full_cells = int(input("Enter number of full cells: "))
    partial_cells = int(input("Enter number of partial cells: "))
    partial_fraction = float(input("Enter average fraction covered by each partial cell (0 to 1): "))

    if cell_area <= 0 or full_cells < 0 or partial_cells < 0:
        print("Enter valid grid values.")
        return

    if partial_fraction < 0 or partial_fraction > 1:
        print("Partial fraction must be between 0 and 1.")
        return

    grid_area = (full_cells * cell_area) + (partial_cells * cell_area * partial_fraction)
    difference = abs(formula_area - grid_area)

    print("\nResults :")
    print("Formula-Based Area:", round(formula_area, 2))
    print("Grid-Based Area:", round(grid_area, 2))
    print("Difference:", round(difference, 2))

    if difference == 0:
        print("Both methods give the same area.")
    elif formula_area > grid_area:
        print("Formula-based area is greater.")
    else:
        print("Grid-based area is greater.")

formulavsgridareacomparison()