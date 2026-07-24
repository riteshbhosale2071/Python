def objectshape():
    obj = input("Enter a daily object: ").lower()

    if obj == "dice":
        print("Shape: Cube")
    elif obj == "ball":
        print("Shape: Sphere")
    elif obj == "can":
        print("Shape: Cylinder")
    elif obj == "ice cream cone":
        print("Shape: Cone")
    elif obj == "brick":
        print("Shape: Cuboid")
    else:
        print("Object not found.")

objectshape()