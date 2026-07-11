def squaretile():
    floor_area = float(input("Enter floor area: "))
    tile_area = float(input("Enter area of one square tile: "))

    tiles = floor_area / tile_area

    print("Tiles Needed:", int(tiles))

squaretile()