def pizza():
    slices = int(input("Enter total pizza slices: "))

    people = int(input("Enter number of people: "))

    each = slices // people
    
    remaining = slices % people

    print("Slices per Person =", each)

    print("Remaining Slices =", remaining)

pizza()