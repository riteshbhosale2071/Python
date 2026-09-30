def gridbasedareaestimator():
    print("Grid-Based Area Estimator :")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    if rows <= 0 or columns <= 0:
        print("Rows and columns must be greater than zero.")
        return

    cell_area = float(input("Enter area of one grid cell: "))

    if cell_area <= 0:
        print("Cell area must be greater than zero.")
        return

    full_cells = int(input("Enter number of completely covered cells: "))
    partial_cells = int(input("Enter number of partially covered cells: "))

    if full_cells < 0 or partial_cells < 0:
        print("Cell counts cannot be negative.")
        return

    total_cells = rows * columns

    if full_cells + partial_cells > total_cells:
        print("The number of covered cells cannot exceed the grid size.")
        return

    partial_fraction = float(input("Enter average fraction covered for each partial cell (0 to 1): "))

    if partial_fraction < 0 or partial_fraction > 1:
        print("Fraction must be between 0 and 1.")
        return

    full_area = full_cells * cell_area
    partial_area = partial_cells * cell_area * partial_fraction
    estimated_area = full_area + partial_area

    print("\nTotal Grid Cells:", total_cells)
    print("Full Cell Area:", round(full_area, 2))
    print("Partial Cell Area:", round(partial_area, 2))
    print("Estimated Area:", round(estimated_area, 2))

gridbasedareaestimator()