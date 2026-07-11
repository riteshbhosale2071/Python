def floortile():
    floor_length = float(input("Enter floor length: "))
    floor_width = float(input("Enter floor width: "))
    tile_length = float(input("Enter tile length: "))
    tile_width = float(input("Enter tile width: "))

    floor_area = floor_length * floor_width
    tile_area = tile_length * tile_width

    tiles = floor_area / tile_area

    print("Number of Tiles Needed:", int(tiles))

floortile()