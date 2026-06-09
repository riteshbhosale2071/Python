def friend():
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    if name1[0].lower() == name2[0].lower():
        print("Best Friend Match!")

    else:
        print("Not a Match")

friend()