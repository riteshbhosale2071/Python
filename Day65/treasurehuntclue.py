def treasure():
    clues = int(input("Enter total number of clues: "))

    found = int(input("Enter number of clues found: "))

    print("Clues Found =", found)
    
    print("Clues Remaining =", clues - found)

treasure()