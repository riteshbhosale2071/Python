def parallelogramoppositeanglevalidator():
    print("Parallelogram Opposite-Angle Validator :")

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))
    angle4 = float(input("Enter angle 4: "))

    if angle1 == angle3 and angle2 == angle4:
        if angle1 + angle2 + angle3 + angle4 == 360:
            print("Opposite angles are equal.")
            print("The angles satisfy the parallelogram property.")
        else:
            print("Opposite angles are equal, but the total angle sum is invalid.")
    else:
        print("Opposite angles are not equal.")
        print("The angles do not satisfy the parallelogram property.")

parallelogramoppositeanglevalidator()