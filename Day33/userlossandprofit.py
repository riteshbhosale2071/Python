def find():
    cp = int(input("Enter Cost Price: "))
    sp = int(input("Enter Selling Price: "))

    if sp > cp:
        print("Profit")
        print("Profit Amount =", sp - cp)

    elif cp > sp:
        print("Loss")
        print("Loss Amount =", cp - sp)

    else:
        print("No Profit No Loss")

find()