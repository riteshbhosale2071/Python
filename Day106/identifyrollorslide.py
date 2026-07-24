def rollorslide():
    shape = input("Enter 3D shape: ").lower()

    if shape == "sphere" or shape == "cylinder" or shape == "cone":
        print("Roll")
    elif shape == "cube" or shape == "cuboid":
        print("Slide")
    else:
        print("Shape not found.")

rollorslide()