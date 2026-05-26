def create():
    object_name = input("Enter object name: ").lower()

    rolling = ["ball", "wheel", "marble", "cylinder"]
    sliding = ["book", "box", "eraser"]

    if object_name in rolling:
        print(object_name, "can roll")

    elif object_name in sliding:
        print(object_name, "can slide")

    else:
        print("Unknown object")

create()