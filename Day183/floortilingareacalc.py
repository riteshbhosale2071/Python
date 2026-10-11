def floortilingareacalc():
    print("Floor-Tiling Area Calculator :")

    length = float(input("Enter floor length: "))
    width = float(input("Enter floor width: "))
    tile_length = float(input("Enter tile length: "))
    tile_width = float(input("Enter tile width: "))
    wastage_percentage = float(input("Enter extra tile percentage for wastage: "))

    if length <= 0 or width <= 0 or tile_length <= 0 or tile_width <= 0:
        print("All dimensions must be greater than zero.")
        return

    if wastage_percentage < 0:
        print("Wastage percentage cannot be negative.")
        return

    floor_area = length * width
    tile_area = tile_length * tile_width
    exact_tiles = floor_area / tile_area
    required_tiles = int(exact_tiles)

    if exact_tiles > required_tiles:
        required_tiles += 1

    tiles_with_wastage = int(required_tiles * (1 + wastage_percentage / 100))

    if required_tiles * (1 + wastage_percentage / 100) > tiles_with_wastage:
        tiles_with_wastage += 1

    print("\nTiling Summary :")
    print("Floor Area:", round(floor_area, 2), "square units")
    print("Single Tile Area:", round(tile_area, 2), "square units")
    print("Tiles Required Without Wastage:", required_tiles)
    print("Tiles Required With Wastage:", tiles_with_wastage)

    cost_per_tile = float(input("Enter cost per tile: "))

    if cost_per_tile < 0:
        print("Tile cost cannot be negative.")
        return

    total_cost = tiles_with_wastage * cost_per_tile

    print("Estimated Total Tiling Cost:", round(total_cost, 2))

floortilingareacalc()