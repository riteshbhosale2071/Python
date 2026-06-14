def moon():
    phase = input("Enter moon phase number (1-4): ")

    if phase == "1":
        print("New Moon")

    elif phase == "2":
        print("First Quarter")

    elif phase == "3":
        print("Full Moon")

    elif phase == "4":
        print("Last Quarter")

    else:
        print("Invalid Choice")

moon()