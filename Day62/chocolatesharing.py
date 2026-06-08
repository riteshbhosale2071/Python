def sharing():
    chocolates = int(input("Enter total chocolates: "))

    children = int(input("Enter number of children: "))

    each = chocolates // children

    remaining = chocolates % children

    print("Each Child Gets =", each)
    
    print("Remaining Chocolates =", remaining)

sharing()