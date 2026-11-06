import math

def materialrequirement():
    print("Material Requirement Calculator")
    print("1. Calculate Flooring Material")
    print("2. Calculate Wall Painting Material")
    print("3. Calculate Concrete Material")
    print("4. Calculate Brick Requirement")

    choice = input("Enter your choice (1-4): ")

    try:
        if choice == "1":
            length = float(input("Enter floor length (meters): "))
            breadth = float(input("Enter floor breadth (meters): "))
            tile_area = float(input("Enter area of one tile (square meters): "))
            wastage = float(input("Enter wastage percentage: "))

            if length <= 0 or breadth <= 0 or tile_area <= 0 or wastage < 0:
                print("Please enter valid positive measurements.")
                return

            floor_area = length * breadth
            total_area = floor_area * (1 + wastage / 100)
            tiles = math.ceil(total_area / tile_area)

            print("Floor Area:", round(floor_area, 2), "square meters")
            print("Total Tiles Required:", tiles)

        elif choice == "2":
            length = float(input("Enter wall length (meters): "))
            height = float(input("Enter wall height (meters): "))
            coverage = float(input("Enter paint coverage (square meters per litre): "))
            coats = int(input("Enter number of coats: "))

            if length <= 0 or height <= 0 or coverage <= 0 or coats <= 0:
                print("All values must be greater than zero.")
                return

            wall_area = length * height
            paint_required = (wall_area * coats) / coverage

            print("Wall Area:", round(wall_area, 2), "square meters")
            print("Paint Required:", round(paint_required, 2), "litres")

        elif choice == "3":
            length = float(input("Enter length (meters): "))
            breadth = float(input("Enter breadth (meters): "))
            thickness = float(input("Enter thickness (meters): "))

            if length <= 0 or breadth <= 0 or thickness <= 0:
                print("All dimensions must be greater than zero.")
                return

            volume = length * breadth * thickness

            print("Concrete Required:", round(volume, 2), "cubic meters")

        elif choice == "4":
            length = float(input("Enter wall length (meters): "))
            height = float(input("Enter wall height (meters): "))
            thickness = float(input("Enter wall thickness (meters): "))
            brick_volume = float(input("Enter volume of one brick including mortar (cubic meters): "))

            if length <= 0 or height <= 0 or thickness <= 0 or brick_volume <= 0:
                print("All values must be greater than zero.")
                return

            wall_volume = length * height * thickness
            bricks = math.ceil(wall_volume / brick_volume)

            print("Wall Volume:", round(wall_volume, 2), "cubic meters")
            print("Bricks Required:", bricks)

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    except ValueError:
        print("Please enter valid numeric values.")

materialrequirement()