def shape():
    shape = input("Enter road sign shape: ").lower()

    if shape == "circle":
        print("Regulatory Sign")

    elif shape == "triangle":
        print("Warning Sign")

    elif shape == "rectangle":
        print("Information Sign")

    elif shape == "octagon":
        print("Stop Sign")

    else:
        print("Unknown Sign")

shape()